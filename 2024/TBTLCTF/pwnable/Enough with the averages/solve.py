from Crypto.Util.number import long_to_bytes
from pwn import *

X = []
for i in range(20):
    io = remote("0.cloud.chals.io", 10198)
    for _ in range(20 - i):
        io.sendline(b"0")
    io.sendline(b"a")
    io.recvuntil(b"Average score is")
    X.append(float(io.recvline().decode().strip().strip(".")))
    print(X[-1])

print(X)

for i in range(1, len(X)):
    d = int(X[i] * 20 - X[i - 1] * 20)
    d %= 1 << 32
    print(long_to_bytes(d))

"""
TBTL{e4t_Y0ur_vegG13s_1n1714l1z3_y0ur_d4rn_v4r14bl35}
"""
