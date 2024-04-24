from pwn import *
from Crypto.Util.number import *
from hashlib import sha256
from secrets import randbelow


def sign(n, msg, d):
    h = bytes_to_long(sha256(msg).digest())
    k = randbelow(q - 2) + 1
    x = pow(h, k, n)
    r = pow(x, d, n)
    s = pow(h + x, d, n)
    return r, s


io = remote("tamuctf.com", "443", ssl=True, sni="smooth-signatures")

for _ in range(2):
    io.sendlineafter(b"sign:", b"A")
    io.recvuntil(b"signature is")
    r, s = eval(io.recvline())

e = 65537
h = bytes_to_long(sha256(b"A").digest())
n, q = 1, 1
for p in Primes():
    if p.bit_length() > 24:
        break
    if (pow(s, e, p) - (pow(r, e, p) + h)) % p == 0:
        n *= p
        q *= p - 1
        print(p)

d = pow(e, -1, q)
msg = b"What is the flag?"
r, s = sign(n, msg, d)

io.sendlineafter(b"question:", msg)
io.sendlineafter(b"signature:", f"{r},{s}".encode())

io.interactive()
#  The flag is: gigem{sm00th_numb3rs_4r3_345y_70_f4c70r}
