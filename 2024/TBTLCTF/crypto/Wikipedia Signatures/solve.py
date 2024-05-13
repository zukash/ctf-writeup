from Crypto.Util.number import *
from pwn import *

# io = process(["python", "server.py"])
io = remote("0.cloud.chals.io", "31148")


def sign(msg):
    io.sendlineafter(b">", f"2 {msg}".encode())
    return int(io.recvline())


io.recvuntil(b"public key:")
n, e = eval(io.recvline())
io.recvuntil(b"wikipedia-RSA")

m = bytes_to_long(b"I challenge you to sign this message!")
s = sign(m * 2) * pow(sign(2), -1, n) % n

io.sendlineafter(b">", f"1 {s}".encode())
io.interactive()
