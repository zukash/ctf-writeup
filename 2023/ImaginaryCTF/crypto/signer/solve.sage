from binascii import crc32
from Crypto.Util.number import *
from pwn import *


def sign(m):
    io.recvuntil(b"2. Get flag")
    io.sendline(b"1")
    io.recvuntil(b"Enter message:")
    io.sendline(m)
    io.recvuntil(b"Signature:")
    return int(io.recvline())


def get_flag(c):
    io.recvuntil(b"2. Get flag")
    io.sendline(b"2")
    io.recvuntil(b"Enter the signature for the password:")
    io.sendline(str(c).encode())
    io.interactive()
    # io.recvuntil(b"Signature:")
    # return int(io.recvline())


io = remote("signer.chal.imaginaryctf.org", "1337")

io.recvuntil(b"n =")
n = io.recvuntil(b"-")
n = int(n[:-1].strip().replace(b"\n", b""))

PASSWORD = b"give me the flag!!!"
crcp = crc32(PASSWORD)

print(factor(crcp))
# 3 * 7 * 12517 * 13477
print(divisors(crcp))

# c0 = sign(long_to_bytes(3))
# c0 = sign(b"123\xcdesS")
# c1 = sign(long_to_bytes(7 * 12517 * 13477))
# c1 = sign(b"123\x11\xea\x1e\xc9")


c0 = sign(b"brkavfs")
c1 = sign(b"nqnbyy")
c2 = sign(b"tM'>]D,d09")

c0 * c1

print(c0)
print(c1)
print(c2)
get_flag(c0 * c1 * c2 % n)

"""
94339 r/Ym;gN,q"
21 hiligo
21 >t>5+h[~Y3
37551 nqnbyy
94339 aaiuazq
13477 tM'>]D,d09
87619 (f&KM9jT7|
7 brkavfs
94339 [IF)IC-gCJ
283017 ^?@Z5>YP)6
1180841263 x]p|JoXF)6
12517 bxzmtet
"""

# ↓これらでうまくいく

"""
7 brkavfs
37551 nqnbyy
13477 tM'>]D,d09
"""
