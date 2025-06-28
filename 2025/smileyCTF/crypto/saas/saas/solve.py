from math import e, gcd
from pwn import *

io = remote("smiley.cat", 39749)

S = set()
while len(S) < 4:
    io.sendlineafter(b">>>", b"1")
    x = int(io.recvline().strip())
    S.add(x)

S = sorted(S)
assert S[0] == 1
n = S[0] + S[-1]
p = gcd(S[0] + S[1], n)
q = n // p

print(f"p = {p}")
print(f"q = {q}")

e = 0x10001
d = pow(e, -1, (p - 1) * (q - 1))

io.sendlineafter(b">>>", b"\x03")  # ctrl-c

io.recvuntil(b"m = ")
m = int(io.recvline().strip())

io.sendlineafter(b">>>", str(pow(m, d, n)).encode())
io.interactive()
