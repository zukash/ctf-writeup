#!/usr/bin/env python3
import os
from Crypto.Util.number import getPrime, getRandomRange


def isSquare(a, p):
    return pow(a, (p - 1) // 2, p) != p - 1


class SquareRNG(object):
    def __init__(self, p, sa, sb):
        assert sa != 0 and sb != 0
        (self.p, self.sa, self.sb) = (p, sa, sb)
        self.x = 0

    def int(self, nbits):
        v, s = 0, 1
        for _ in range(nbits):
            self.x = (self.x + 1) % p
            s += pow(self.sa, self.x, self.p) * pow(self.sb, self.x, self.p)
            s %= self.p
            #############
            if self.sb == 1 and self.x == 32:
                v = (pow(self.sa, 33, p) - 1) % p
                assert v == (self.sa - 1) * s % p
                # isSquare(v, p) を聞かれる
                c1 = isSquare(v, p)
                c2 = isSquare(self.sa - 1, p)
                c3 = isSquare(s, p)
                assert c1 & 1 != (c2 + c3) & 1
                # 以下が成立するのは isSquare(-1, p) == 1 のときだが、珍しくない
                # また、p は全てのラウンドで共通なので、全部間違えるか・全部正解するかのどちらか
                c2_ = isSquare(1 - self.sa, p)
                assert c1 & 1 != (c2_ + c3) & 1
            #############
            v = (v << 1) | int(isSquare(s, self.p))
        return v

    def bool(self):
        self.x = (self.x + 1) % self.p
        print(self.x)
        t = pow(self.sa, self.x, self.p) + pow(self.sb, self.x, self.p)
        t %= self.p
        return isSquare(t, self.p)


p = getPrime(256)

sb1 = int(input("Bob's seed 1: ")) % p
sb2 = int(input("Bob's seed 2: ")) % p
for _ in range(77):
    sa = getRandomRange(1, p)
    # sa = getRandomRange(1, 10)
    r1 = SquareRNG(p, sa, sb1)
    n1 = r1.int(32)
    print("Random 1:", f"{n1:032b}")
    r2 = SquareRNG(p, sa, sb2)
    n2 = r2.int(32)
    print("Random 2:", f"{n2:032b}")

    # guess = int(input("Guess next bool [0 or 1]: "))
    g1 = n1 >> 31 & 1
    g2 = n2 & 1
    guess = ((g1 + g2) & 1) ^ 1
    if guess == int(r1.bool()):
        print("OK!")
    else:
        print("NG...")
        break
else:
    print("Congratz!")
    print(os.getenv("FLAG", "nek0pts{*** REDACTED ***}"))
