# Baby-step Giant-step法
def babystep_giantstep(g, y, p, q=None):
    if q is None:
        q = p - 1
    m = int(q ** 0.5 + 0.5)
    # Baby step
    table = {}
    gr = 1  # g^r
    for r in range(m):
        table[gr] = r
        gr = (gr * g) % p
    # Giant step
    try:
        gm = pow(g, -m, p)  # gm = g^{-m}
    except:
        return None
    ygqm = y  # ygqm = y * g^{-qm}
    for q in range(m):
        if ygqm in table:  # 左辺と右辺が一致するとき
            return q * m + table[ygqm]
        ygqm = (ygqm * gm) % p
    return None


# Pohlig–Hellman法
def pohlig_hellman_DLP(g, y, p):
    crt_moduli = []
    crt_remain = []
    for q, _ in factor(p - 1):
        x = babystep_giantstep(pow(g, (p - 1) // q, p), pow(y, (p - 1) // q, p), p, q)
        if (x is None) or (x <= 1):
            continue
        crt_moduli.append(q)
        crt_remain.append(x)
    x = crt(crt_remain, crt_moduli)
    return x


g = 2
y = 1094511311619717224471473901707
p = (
    0xD2F8711CB5502C512ACEA59BE181A8FCF12F183B540D9A6998BF66370F9538F7E39FC507545DAD9AA2E71D3313F0B4408695A0A2C03A790662A9BD01650533C584C90779B73604FB8157F0AB7C9A82E724700E5937D9FF5FCF1EE3BE1EDD7E07B4C0F035A58CC2B9DB8B79F176F595C1B0E90B7957309B96106A50A01B78171599B41C8744BCB1C0E6A24F60AE8946D37F4D4BD8CF286A336E1022996B3BA3918E4D808627D0315BFE291AEB884CBE98BB620DAA735B0467F3287D158231D
    + 1
)
# p = 2 * 32803 * 196159 * 1981991353 * 47814426923 + 1  # 素数p
x = pohlig_hellman_DLP(g, y, p)
print(x)
print(pow(g, x, p) == y)
