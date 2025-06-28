# https://github.com/Legrandin/pycryptodome/blob/master/lib/Crypto/Cipher/_mode_gcm.py
# ref. https://furutsuki.hatenablog.com/entry/2022/03/27/105150
# ref. https://jovi0608.hatenablog.com/entry/20160524/1464054882
# ref. https://kmyk.github.io/blog/writeups/ctf-2018-volgactf-2018-quals-forbidden/
# ref. https://zenn.dev/anko/articles/ctf-crypto-commonkey
# ref. https://meowmeowxw.gitlab.io/ctf/utctf-2020-crypto/

from sage.all import *
from pwn import *
import secrets
from Crypto.Cipher import AES


def to_poly(x):
    bs = Integer(int.from_bytes(x, "big")).bits()[::-1]
    return F([0] * (128 - len(bs)) + bs)


def to_bytes(poly):
    return int(bin(poly.integer_representation())[2:].zfill(128)[::-1], 2).to_bytes(
        16, "big"
    )


keys = [secrets.token_bytes(16) for _ in range(2)]
nonce = secrets.token_bytes(16)


def summon(number, plaintext):
    assert len(plaintext) == 16
    aes = AES.new(key=keys[number - 1], mode=AES.MODE_GCM, nonce=nonce)
    _, tag = aes.encrypt_and_digest(plaintext)
    return tag


def summon(number, plaintext):
    io.sendlineafter(b">", b"1")
    io.sendlineafter(b">", str(number).encode())
    io.sendlineafter(b">", plaintext.hex())
    return bytes.fromhex(
        io.recvline_contains(b"tag(hex) = ").split(b"=")[1].strip().decode()
    )


def dual_summon(plaintext):
    io.sendlineafter(b">", b"2")
    io.sendlineafter(b">", plaintext.hex())
    io.interactive()


# context.log_level = "DEBUG"
io = remote("dual-summon.seccon.games", 2222)


R = PolynomialRing(GF(2), "x")
x = R.gen()
F = GF(2**128, "a", modulus=x**128 + x**7 + x**2 + x + 1)
a = F.gen()
PR = PolynomialRing(F, "x")
x = PR.gen()

PX = b"X" * 16
PY = b"Y" * 16
PXY = xor(PX, PY)

T1X = summon(1, PX)
T1Y = summon(1, PY)
T1XY = summon(1, PXY)
T2X = summon(2, PX)
T2Y = summon(2, PY)
T2XY = summon(2, PXY)

D1 = xor(T1XY, xor(T1X, T1Y))
D2 = xor(T2XY, xor(T2X, T2Y))

h1 = to_poly(xor(T1X, D1)) / to_poly(PX)
assert h1 == to_poly(xor(T1Y, D1)) / to_poly(PY)
h2 = to_poly(xor(T2X, D2)) / to_poly(PX)
assert h2 == to_poly(xor(T2Y, D2)) / to_poly(PY)

p = to_poly(xor(D1, D2)) / (h1 + h2)
P = to_bytes(p)

dual_summon(P)
