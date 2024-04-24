import random
from itertools import product

############## secret ###################
p = 158982482761532936352511330658816601706429032258548834912125273034488997046490434244533210801707343036413253864390713073589522875165458597351216083121996049787719375116167821890856038886439850595034188390482176192712663134014807479657958971828756944383908361170612935098217276884087156156071510999037803600539
q = 175034578077309701984181964268308339398388268617712324238289276804454728925416562859929986131078776699682249344599789995987665924833218204252743836262945362936105111796551388997258331666189228142473360653861656406464150833269243661900931849107877401563507303666653995787300006491378116771557849415731270875381
#########################################

def random_mask(p):
    k = p.bit_length()
    mask = random.sample(range(k), k = int(k * 0.51))
    mask = sum(1 << i for i in mask)
    return mask, mask & p

# generate hints
m0, h0 = random_mask(p)
m1, h1 = random_mask(q)
n = p * q
p, q = None, None
#########################################

def equiv(x, y, m):
    return x & (m - 1) == y & (m - 1)
    # return x % m == y % m

def check(p, q, n, h0, h1, k):
    m = 1 << k
    return equiv(p * q, n, m) and equiv(p & m0, h0, m) and equiv(q & m1, h1, m)
def fast_check(p, q, n, h0, h1, k):
    m = (1 << k) - 1
    p &= m
    q &= m
    n &= m
    return equiv(p * q, n, m) and equiv(p & m0, h0, m) and equiv(q & m1, h1, m)


def factor(n, h0, h1):
    assert check(1, 1, n, h0, h1, 1)
    cand = {(1, 1)}
    for k in range(2, 2049):
        bit = 1 << (k - 1)
        ncand = set()
        for p, q in cand:
            for np, nq in product([p, p | bit], [q, q | bit]):
                if fast_check(np, nq, n, h0, h1, k):
                    ncand.add((np, nq))
            if p * q == n:
                return p, q
        cand = ncand
        print(k, len(cand))

p, q = factor(n, h0, h1)
print(f'{p = }')
print(f'{q = }')
assert p * q == n