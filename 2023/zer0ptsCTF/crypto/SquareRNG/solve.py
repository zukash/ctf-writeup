from pwn import *

io = remote("crypto.2023.zer0pts.com", "10666")

io.recvuntil(b"Bob's seed 1:")
io.sendline(b"-1")
io.recvuntil(b"Bob's seed 2:")
io.sendline(b"1")

for _ in range(77):
    io.recvuntil(b"Random 1:")
    n1 = int(io.recvline(), 16)
    io.recvuntil(b"Random 2:")
    n2 = int(io.recvline(), 16)

    g1 = n1 >> 31 & 1
    g2 = n2 & 1
    guess = ((g1 + g2) & 1) ^ 1
    io.sendline(str(guess).encode())
    print(io.recvline())


io.interactive()
