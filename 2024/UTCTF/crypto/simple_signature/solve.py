from pwn import *

# nc betta.utctf.live 4374
io = remote("betta.utctf.live", 4374)


def io_get_param():
    io.recvuntil(b"n = ")
    n = int(io.recvline())
    io.recvuntil(b"e = ")
    e = int(io.recvline())
    return n, e


def io_sign(m):
    io.sendlineafter(b"(enter 0 to stop):", str(m).encode())
    io.recvuntil(b"Your signature is:")
    return int(io.recvline())


def io_verify(m, s):
    io.sendlineafter(b"message:", str(m).encode())
    io.sendlineafter(b"signature:", str(s).encode())


n, e = io_get_param()
s2 = io_sign(2)
io.sendlineafter(b":", b"0")
io_verify(1, s2)

io.interactive()
