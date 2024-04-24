from functools import lru_cache
from Crypto.Util.number import *
from math import isqrt
import sys

sys.setrecursionlimit(10 ** 8)

N = 180501716611818439995609435542731470075775193176428263372546170684067831289410

###################################
# https://math.stackexchange.com/questions/5877/efficiently-finding-two-squares-which-sum-to-a-prime
def mods(a, n):
    if n <= 0:
        return "negative modulus"
    a = a % n
    if 2 * a > n:
        a -= n
    return a


def powmods(a, r, n):
    out = 1
    while r > 0:
        if (r % 2) == 1:
            r -= 1
            out = mods(out * a, n)
        r //= 2
        a = mods(a * a, n)
    return out


def quos(a, n):
    if n <= 0:
        return "negative modulus"
    return (a - mods(a, n)) // n


def grem(w, z):
    # remainder in Gaussian integers when dividing w by z
    (w0, w1) = w
    (z0, z1) = z
    n = z0 * z0 + z1 * z1
    if n == 0:
        return "division by zero"
    u0 = quos(w0 * z0 + w1 * z1, n)
    u1 = quos(w1 * z0 - w0 * z1, n)
    return (w0 - z0 * u0 + z1 * u1, w1 - z0 * u1 - z1 * u0)


def ggcd(w, z):
    while z != (0, 0):
        w, z = z, grem(w, z)
    return w


def root4(p):
    # 4th root of 1 modulo p
    if p <= 1:
        return "too small"
    if (p % 4) != 1:
        return "not congruent to 1"
    k = p // 4
    j = 2
    while True:
        a = powmods(j, k, p)
        b = mods(a * a, p)
        if b == -1:
            return a
        if b != 1:
            return "not prime"
        j += 1


def sq2(p):
    a = root4(p)
    return ggcd((p, 0), (a, 1))


print(sq2(157))
##############################


@lru_cache(None)
def decompose(p2_q2):
    """
    (a2 + b2) * (c2 + d2) == (ac + bd)^2 + (ad - bc)^2 に基づいて、
    (p, q) = (ac + bd, ad - bc) を返す
    """
    ans = []
    if p2_q2 <= 100:
        for p in range(101):
            q2 = p2_q2 - p ** 2
            if q2 < 0:
                continue
            q = isqrt(q2)
            if p ** 2 + q ** 2 != p2_q2:
                continue
            ans.append((p, q))
            # if not (is_prime(p) and is_prime(q)):
            #     continue
        return ans

    if isqrt(p2_q2) ** 2 == p2_q2:
        p_q = isqrt(p2_q2)
        ans.append((0, p_q))
        ans.append((p_q, 0))

    if is_prime(p2_q2) and p2_q2 % 4 == 1:
        p, q = sq2(p2_q2)
        assert p ** 2 + q ** 2 == p2_q2
        ans.append((p, q))
        ans.append((q, p))

    for a2_b2 in divisors(p2_q2):
        c2_d2 = p2_q2 // a2_b2
        if a2_b2 == 1 or c2_d2 == 1:
            continue
        assert a2_b2 * c2_d2 == p2_q2
        AB = decompose(a2_b2)
        CD = decompose(c2_d2)
        # print(a2_b2, AB)
        # print(c2_d2, CD)
        if not (AB and CD):
            continue
        for ab in AB:
            for cd in CD:
                a, b = ab
                c, d = cd
                left = (a ** 2 + b ** 2) * (c ** 2 + d ** 2)
                right = (a * c - b * d) ** 2 + (a * d + b * c) ** 2
                if left != right:
                    continue
                ans.append((a * c - b * d, a * d + b * c))
        for ab in AB:
            for cd in CD:
                a, b = ab
                c, d = cd
                left = (a ** 2 + b ** 2) * (c ** 2 + d ** 2)
                right = (a * c + b * d) ** 2 + (a * d - b * c) ** 2
                if left != right:
                    continue
                ans.append((a * c + b * d, a * d - b * c))
    return list(set(ans))


for p, q in decompose(N):
    if p < 0 or q < 0:
        continue
    if not (p.bit_length() == q.bit_length() == 128):
        continue
    if not (is_prime(p) and is_prime(q)):
        continue
    print(p, q)
