from pwn import *
from Crypto.Util.number import long_to_bytes

# nc third-times-the-charm.ctf.umasscybersec.org 1337
io = remote("third-times-the-charm.ctf.umasscybersec.org", "1337")
# io = process(["python", "main.py"])

# io.interactive()

io.recvuntil(b"m1:")
m1 = int(io.recvline())
io.recvuntil(b"N1:")
N1 = int(io.recvline())

io.recvuntil(b"m2:")
m2 = int(io.recvline())
io.recvuntil(b"N2:")
N2 = int(io.recvline())

io.recvuntil(b"m3:")
m3 = int(io.recvline())
io.recvuntil(b"N3:")
N3 = int(io.recvline())

mmm = crt([m1, m2, m3], [N1, N2, N3])
m = int(mmm ^ (1 / 3))
print(long_to_bytes(m))
