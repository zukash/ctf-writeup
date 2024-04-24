from Crypto.Util.number import *
from pwn import *

while True:
    io = remote("morphing.chal.uiuc.tf", int(1337))
    print(io.recvline())
    print(io.recvline())
    print(io.recvline())

    g = int(io.recvline().split(b"=")[-1])
    p = int(io.recvline().split(b"=")[-1])
    A = int(io.recvline().split(b"=")[-1])
    print(g, p, A)

    print(io.recvline())
    c1 = int(io.recvline().split(b"=")[-1])
    c2 = int(io.recvline().split(b"=")[-1])
    print(c1, c2)

    c1_ = c2_ = pow(g, (p - 1) // 2, p)
    if c1 * c1_ % p == c1 and c2 * c2_ % p == c2:
        break
    io.close()

assert c1 * c1_ == c1
assert c2 * c2_ == c2

print("++++++++++++++++++++++++++++++")
print(c1_)
print(c2_)
print("++++++++++++++++++++++++++++++")
io.sendline(str(c1_).encode())
io.sendline(str(c2_).encode())
io.recvuntil(b"m = ")
io.interactive()

print()
m = int(io.recvline())
print(m)
print(long_to_bytes(m))
print()

io.interactive()


# # io.recvline(b"=")
# # p = int(io.recvline())

# # io.recvline(b"=")
# # A = int(io.recvline())

# # print(g, p, A)
