from Crypto.Util.number import *
from subprocess import check_output, CalledProcessError
from re import findall
import itertools
from tqdm import tqdm

def flatter(M):
    try:
        z = "[[" + "]\n[".join(" ".join(map(str, row)) for row in M) + "]]"
        ret = check_output(["flatter"], input=z.encode())
        return matrix(M.nrows(), M.ncols(), map(int, findall(b"-?\\d+", ret)))
    except:
        return M.LLL()


RRh = RealField(5000)


def solve_root_jacobian_newton_internal(pollst, startpnt, maxiternum=500):
    # NOTE: Newton method's complexity is larger than BFGS, but for small variables Newton method converges soon.
    pollst_Q = Sequence(pollst, pollst[0].parent().change_ring(QQ))
    vars_pol = pollst_Q[0].parent().gens()
    jac = jacobian(pollst_Q, vars_pol)

    if all([ele == 0 for ele in startpnt]):
        # just for prepnt != pnt
        prepnt = {vars_pol[i]: 1 for i in range(len(vars_pol))}
    else:
        prepnt = {vars_pol[i]: 0 for i in range(len(vars_pol))}
    pnt = {vars_pol[i]: startpnt[i] for i in range(len(vars_pol))}

    iternum = 0
    while True:
        if iternum >= maxiternum:
            return None

        evalpollst = [(pollst_Q[i].subs(pnt)) for i in range(len(pollst_Q))]
        if all([int(ele) == 0 for ele in evalpollst]):
            break
        jac_eval = jac.subs(pnt)
        evalpolvec = vector(QQ, len(evalpollst), evalpollst)
        try:
            pnt_diff_vec = jac_eval.solve_right(evalpolvec)
        except:
            return None

        prepnt = {key:value for key,value in prepnt.items()}
        pnt = {vars_pol[i]: int(pnt[vars_pol[i]] - pnt_diff_vec[i]) for i in range(len(pollst_Q))}
        if all([prepnt[vars_pol[i]] == pnt[vars_pol[i]] for i in range(len(vars_pol))]):
            return None
        prepnt = {key:value for key,value in pnt.items()}
        iternum += 1
    return [int(pnt[vars_pol[i]]) for i in range(len(vars_pol))]


def solve_root_jacobian_newton(pollst, bounds):
    vars_pol = pollst[0].parent().gens()
    # not applicable to non-determined system
    if len(vars_pol) > len(pollst):
        return []
    # pollst is not always algebraically independent,
    # so just randomly choose wishing to obtain an algebraically independent set
    for random_subset in tqdm(Combinations(pollst, k=len(vars_pol))): 
        for signs in itertools.product([1, -1], repeat=len(vars_pol)):
            startpnt = [signs[i] * bounds[i] for i in range(len(vars_pol))]
            result = solve_root_jacobian_newton_internal(random_subset, startpnt)
            # filter too much small solution
            if result is not None:
                if all([abs(ele) < 2**16 for ele in result]):
                    continue
                return [result]


def gen_set_leading_monomials(basepoly):
    if basepoly.is_constant():
        return [basepoly.parent()(1)]

    lmset = [basepoly.parent()(1)]
    for monomial in basepoly.monomials():
        newlmfound = True
        newlmset = []
        for lmsetele in lmset:
            if monomial % lmsetele != 0:
                newlmset.append(lmsetele)
            if lmsetele % monomial == 0:
                newlmfound = False
        if newlmfound:
            newlmset.append(monomial)
        lmset = newlmset[:]
    return lmset


def generate_M_with_ExtendedStrategy(basepoly, lm, t, d):
    basepoly_vars = basepoly.parent().gens()
    n = len(basepoly_vars)

    M = {}
    basepoly_pow_monos = (basepoly ** t).monomials()
    for k in range(t+1):
        M[k] = set()
        basepoly_powk_monos = (basepoly ** (t - k)).monomials()
        for monos in basepoly_pow_monos:
            if monos // (lm ** k) in basepoly_powk_monos:
                for extra in itertools.product(range(d), repeat=n):
                    g = monos * prod([v ** i for v, i in zip(basepoly_vars, extra)])
                    M[k].add(g)
    M[t+1] = set()
    return M

def shiftpoly(basepoly, baseidx, Nidx, varsidx_lst):
    N = basepoly.parent().characteristic()
    basepoly_ZZ = basepoly.change_ring(ZZ)
    vars_ZZ = basepoly_ZZ.parent().gens()
    if len(vars_ZZ) != len(varsidx_lst):
        raise ValueError("varsidx_lst len is invalid (on shiftpoly)")
    return (basepoly_ZZ ** baseidx) * (N ** Nidx) * prod([v ** i for v, i in zip(vars_ZZ, varsidx_lst)])


def monomialset(fis):
    m_set = set()
    for fi in fis:
        m_set = m_set.union(set(fi.monomials()))
    return m_set


def genmatrix_from_shiftpolys(shiftpolys, bounds):
    m_lst = list(monomialset(shiftpolys))
    vars_ZZ = shiftpolys[0].parent().gens()
    if len(vars_ZZ) != len(bounds):
        raise ValueError("bounds len is invalid (on genmatrix_from_shiftpolys)")
    matele = []
    for sftpol in shiftpolys:
        sftpol_sub_bound = sftpol.subs({vars_ZZ[i]: vars_ZZ[i]*bounds[i] for i in range(len(vars_ZZ))})
        matele += [sftpol_sub_bound.monomial_coefficient(m_lst[i]) for i in range(len(m_lst))]
    mat = matrix(ZZ, len(matele)//len(m_lst), len(m_lst), matele)
    return mat, m_lst

def filter_LLLresult_coppersmith(basepoly, t, m_lst, lll, bounds, beta=1.0):
    vars_ZZ = m_lst[0].parent().gens()
    N = basepoly.parent().characteristic()
    howgrave_bound = (RRh(N)**RRh(beta))**RRh(t)
    if len(m_lst) != lll.ncols():
        raise ValueError("lll or trans result is invalid (on filter_LLLresult_coppersmith)")
    # use vector (not use matrix norm, but vector norm)
    lll_vec = lll.rows()

    m_lst_bound = [m_lstele.subs({vars_ZZ[i]: bounds[i] for i in range(len(vars_ZZ))}) for m_lstele in m_lst]

    result = []
    for lll_vecele in lll_vec:
        if all([int(lll_vecele_ele) == 0 for lll_vecele_ele in lll_vecele]):
            continue
        lll_l1norm = lll_vecele.norm(p=1)
        if lll_l1norm >= howgrave_bound:
            continue
        howgrave_ratio = int(((lll_l1norm/howgrave_bound)*(10**15))*(0.1**15))
        pol = 0
        for j, m_lstele_bound in enumerate(m_lst_bound):
            #assert int(lll_vecele[j]) % int(m_lstele_bound) == 0
            pol += (int(lll_vecele[j]) // int(m_lstele_bound)) * m_lst[j]
        result.append(pol)
    return result


### multivariate coppersmith with some heuristic (jochemsz-may)
def coppersmith_multivariate_heuristic_core(basepoly, bounds, t, d, lm, maxmatsize=100):
    print("trying param: t=%d, d=%d, lm=%s" % (t, d, str(lm)))
    basepoly_vars = basepoly.parent().gens()
    n = len(basepoly_vars)
    basepoly_i = basepoly * (1 / basepoly.monomial_coefficient(lm))
    M = generate_M_with_ExtendedStrategy(basepoly_i, lm, t, d)
    shiftpolys = []
    for k in range(t+1):
        for mono in M[k] - M[k+1]:
            curmono = (mono // (lm ** k))
            xi_idx = curmono.exponents()[0]
            shiftpolys.append(shiftpoly(basepoly_i, k, t - k, xi_idx))

    mat, m_lst = genmatrix_from_shiftpolys(shiftpolys, bounds)
    if mat.ncols() > maxmatsize:
        print("maxmatsize exceeded: %d" % mat.ncols())
        return []

    print('LLL start...')
    try:
        lll = flatter(mat)
    except CalledProcessError:
        print('flatter crashed')
        return []
    print('LLL done')
    result = filter_LLLresult_coppersmith(basepoly, t, m_lst, lll, bounds)
    return result


def coppersmith_multivariate_heuristic(basepoly, bounds, maxd=8):
    # auto-tries different t and d
    N = basepoly.parent().characteristic()
    basepoly_vars = basepoly.parent().gens()
    n = len(basepoly_vars)
    if n == 1:
        raise ValueError("one variable poly")
    lms = gen_set_leading_monomials(basepoly)
    basepoly_ZZ_vars = basepoly.change_ring(ZZ).parent().gens()
    t = 2
    curfoundpols = []
    while True:
        d0 = t
        for d_diff in range(0, maxd+1):
            d = d0 + d_diff
            for lm in lms:
                foundpols = coppersmith_multivariate_heuristic_core(basepoly, bounds, t, d, lm, maxmatsize=100)
                if len(foundpols) == 0:
                    continue
                curfoundpols += foundpols
                curfoundpols = list(set(curfoundpols))
                sol = solve_root_jacobian_newton(curfoundpols, bounds)
                if sol != [] and sol is not None:
                    return sol
        t += 1

def coppersmith_multivariate_direct(basepoly, bounds, t=2, d=2):
    N = basepoly.parent().characteristic()
    basepoly_vars = basepoly.parent().gens()
    n = len(basepoly_vars)
    if n == 1:
        raise ValueError("one variable poly")
    lms = gen_set_leading_monomials(basepoly)
    basepoly_ZZ_vars = basepoly.change_ring(ZZ).parent().gens()
    curfoundpols = []
    for lm in lms:
        foundpols = coppersmith_multivariate_heuristic_core(basepoly, bounds, t, d, lm, maxmatsize=100)
        if len(foundpols) == 0:
            continue
        curfoundpols += foundpols
        curfoundpols = list(set(curfoundpols))
        sol = solve_root_jacobian_newton(curfoundpols, bounds)
        if sol != [] and sol is not None:
            return sol


def daisy_bell_bi0sCTF_2024():
    n = 13588728652719624755959883276683763133718032506385075564663911572182122683301137849695983901955409352570565954387309667773401321714456342417045969608223003274884588192404087467681912193490842964059556524020070120310323930195454952260589778875740130941386109889075203869687321923491643408665507068588775784988078288075734265698139186318796736818313573197531378070122258446846208696332202140441601055183195303569747035132295102566133393090514109468599210157777972423137199252708312341156832737997619441957665736148319038440282486060886586224131974679312528053652031230440066166198113855072834035367567388441662394921517
    c = 7060838742565811829053558838657804279560845154018091084158194272242803343929257245220709122923033772911542382343773476464462744720309804214665483545776864536554160598105614284148492704321209780195710704395654076907393829026429576058565918764797151566768444714762765178980092544794628672937881382544636805227077720169176946129920142293086900071813356620614543192022828873063643117868270870962617888384354361974190741650616048081060091900625145189833527870538922263654770794491259583457490475874562534779132633901804342550348074225239826562480855270209799871618945586788242205776542517623475113537574232969491066289349
    p_high = 914008410449727213564879221428424249291351166169082040257173225209300987827116859791069006794049057028194309080727806930559540622366140212043574
    u_low = 233711553660002890828408402929574055694919789676036615130193612611783600781851865414087175789069599573385415793271613481055557735270487304894489126945877209821010875514064660591650207399293638328583774864637538897214896592130226433845320032466980448406433179399820207629371214346685408858
    q_high = n // (p_high<<545)
    PR.<x, y> = PolynomialRing(Zmod(n), 2)
    qq = q_high + x
    uu = y * 2**955 + u_low
    f = uu*qq**2 - qq  
    bounds = (2**545, 2**(1024-955))
    q_low, u_high = coppersmith_multivariate_direct(f, [2**545, 2**68], t=2, d=4)[0]
    q = int(qq(x=q_low))
    print(long_to_bytes(int(pow(c, pow(65537, -1, (n//q-1)*(q-1)), n))))

def dp_high_ISITDTU_CTF_2022():
    n = 12567364021021536069276139071081301321773783503415410122482063162815802632532262852631733566943908930876147793969043836275748336698486250666608690152319164539308799173942970880405365621942480869038031173565836135609803219607046250197218934622063531043191571238635559343630285434743137661162918049427668167596108116123813247574023489647941191092646108484359798178312183857161198552950237016232564837163103701319852345468700518013420435831423503394375188294692875472478236076844354332788143724582596188171429101120375457060113120938123836683660988201443089327738905824392062439034247838606482384586412614406834714072187
    e = 302855054306017053454220113135236383717
    c = 4891864668386517178603039798367030027018213726546115291869063934737584262406041165900191539273508747711632172112784295237035437771196319634059866827443546543304905951054697225192869131382430968922874630769470296997764149219967748222295126835357440172029624432839432442542014919311928847815297342723030801298870843985791566021870092065045427815279776382037308098892891521540483210118257005467504087917529931331454698510489305696908930175868148922286615019210097019743367080206300230172144203634385318929457785251214794930401419137018353777022634635240368493042317181737723067635048719777029127030494920756862174788399
    dp_high = 1528682061327606941204027235121547734644486174542891631806426376137001818312801429494781262718713071077103179054205712581085921624900599327139049785998451580793229375262096344994664540984947702348067124539258177759586538935334513702134177319291812
    PR.<x,k> = PolynomialRing(Zmod(n), 2)
    f = 1 - k - ((dp_high << 205) + x) * e
    roots = coppersmith_multivariate_direct(f, [2**205, 2**128], t=2, d=3)
    if roots is None:
        print('fail')
        return False
    x, k = roots[0]
    p = gcd(int(f(x, k)), n)
    q = int(n) // int(p)
    d = pow(e, -1, (p-1)*(q-1))
    m = pow(c, int(d), n)
    print(long_to_bytes(int(m)))
    return True

def tests():
    daisy_bell_bi0sCTF_2024()
    dp_high_ISITDTU_CTF_2022()

#tests()