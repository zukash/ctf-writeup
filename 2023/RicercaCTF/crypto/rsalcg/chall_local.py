from Crypto.Util.number import getPrime, getRandomNBitInteger
import os

SIZE = 32
FLAG = os.getenv("FLAG", "RicSec{dummy}").encode()


def RSALCG(a, b, n):
    e = 3
    s = getRandomNBitInteger(SIZE * 2) % n
    while True:
        s = (a * s + b) % n
        print(f"{s = }")
        yield pow(s, e, n)


def encrypt(rand, msg):
    print(msg)
    assert len(msg) < (SIZE // 2)
    m = int.from_bytes(msg, "big")
    r = next(rand)
    print(f"{m = }")
    print(f"{r = }")
    return int.to_bytes(m ^ r, (SIZE // 2), "big")


if __name__ == "__main__":
    n = getPrime(SIZE) * getPrime(SIZE)
    a = getRandomNBitInteger(SIZE * 2)
    b = getRandomNBitInteger(SIZE * 2)
    rand = RSALCG(a, b, n)
    print(f"{a = }")
    print(f"{b = }")
    print(f"{n = }")

    m1 = b"hoge"
    m3 = b"fuga"

    # given
    c1 = encrypt(rand, m1).hex()
    c2 = encrypt(rand, FLAG).hex()
    c3 = encrypt(rand, m3).hex()

    # to int
    m1 = int.from_bytes(m1, "big")
    m3 = int.from_bytes(m3, "big")
    c1 = int(c1, 16)
    c2 = int(c2, 16)
    c3 = int(c3, 16)
    print(f"{c1 = }")
    print(f"{c2 = }")
    print(f"{c3 = }")

    r1 = m1 ^ c1
    r3 = m3 ^ c3

    e = 3
    print(f"{r1 = }")
    print(f"{r3 = }")
    print(f"{e = }")
    print(f"{n = }")
    print(f"{a = }")
    print(f"{b = }")


# print(franklinreiter(r3, r1, e, n, a, b))
