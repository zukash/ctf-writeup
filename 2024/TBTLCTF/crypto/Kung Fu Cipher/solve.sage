from pwn import *
from Crypto.Util.number import long_to_bytes
from itertools import product

io = process(["sage", "server.py"])
# io = remote("0.cloud.chals.io", "30461")
io.recvuntil(b"n = ")
n = int(io.recvline(), 16)
print(n)

# ******************************************************
# specify e
# ******************************************************
io.sendlineafter(b">", b"2")
io.sendline(b"1")
io.sendline(b"1")
io.sendline(b"0")
io.sendline(b"1")
io.recvuntil(b"ct[0][1] = ")
e = int(io.recvline(), 16)

# ******************************************************
# factor n
# ******************************************************
X = [("", "")]
for i in range(1, 81):
    nX = []
    while X:
        x, y = X.pop()
        for dx, dy in product(["5", "7", "9"], repeat=2):
            nx = int(dx + x)
            ny = int(dy + y)
            if (n - (nx * ny)) % pow(10, i) == 0:
                nX.append((str(nx), str(ny)))
    X = nX

for p, q in X:
    p, q = int(p), int(q)
    if p * q == n:
        break

assert p * q == n

print(f"{n = }")
print(f"{p = }")
print(f"{q = }")
print(f"{e = }")

# ******************************************************
# decrypt
# ******************************************************
io.sendlineafter(b">", b"1")

ct = []

io.recvuntil(b"ct[0][0] = ")
ct.append(int(io.recvline(), 16))

io.recvuntil(b"ct[0][1] = ")
ct.append(int(io.recvline(), 16))

io.recvuntil(b"ct[1][0] = ")
ct.append(int(io.recvline(), 16))

io.recvuntil(b"ct[1][1] = ")
ct.append(int(io.recvline(), 16))

M = matrix(Zmod(n), 2, 2, ct)
d = pow(e, -1, (p - 1) * (q - 1))
M = M**d

for i in range(2):
    for j in range(2):
        print(long_to_bytes(int(M[i][j])).decode(), end="")

io.interactive()
