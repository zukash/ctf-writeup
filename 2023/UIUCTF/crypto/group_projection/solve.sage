from pwn import *

while True:
    io = remote("group-projection.chal.uiuc.tf", int(1337))

    io.recvuntil(b"g = ")
    g = int(io.recvline())

    io.recvuntil(b"p = ")
    p = int(io.recvline())

    io.recvuntil(b"A = ")
    A = int(io.recvline())

    io.recvuntil(b"k = ")

    print(f"{p=}")
    print(f"{g=}")
    print(f"{A=}")
    k = (p - 1) // 4
    if pow(g, k, p) == 1:
        io.sendline(str(k).encode())
        io.interactive()
    io.close()
