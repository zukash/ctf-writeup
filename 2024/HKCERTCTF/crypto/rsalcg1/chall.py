import os
from functools import reduce
from operator import mul
import secrets
from Crypto.Util.number import isPrime as is_prime


class LCG:
    def __init__(self, bits, a=None, c=None, seed=None):
        self.seed = seed
        if self.seed is None:
            self.seed = secrets.randbits(bits) | 1
        self.a = a
        if self.a is None:
            self.a = secrets.randbits(bits) | 1
        self.c = c
        if self.c is None:
            self.c = secrets.randbits(bits)
        self.bits = bits
        self.m = 2**bits

    def next(self):
        self.seed = (self.seed * self.a + self.c) % self.m
        return self.seed

    def __repr__(self):
        return f"LCG(bits={self.bits}, a={self.a}, c={self.c})"


def get_prime(lcg, bits):
    while True:
        p = 0
        for i in range(bits // lcg.bits):
            p <<= lcg.bits
            p |= lcg.next()

        if p.bit_length() != bits:
            continue
        if not is_prime(p):
            continue

        return p


if __name__ == "__main__":
    FLAG = os.environb.get(b"FLAG", b"hkcert24{***REDACTED***}")

    lcg = LCG(bits=256, c=0)

    print(f"{lcg = }")
    print(f"{lcg.seed = }")

    ps = [get_prime(lcg, bits=1024) for _ in range(4)]
    print(ps)
    n = reduce(mul, ps)
    e = 0x10001

    m = int.from_bytes(FLAG, "big")
    c = pow(m, e, n)

    print(f"{n = }")
    print(f"{e = }")
    print(f"{c = }")
