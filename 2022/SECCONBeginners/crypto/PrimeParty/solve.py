from pwn import *
from Crypto.Util.number import *

io = process(["python", "server.py"])

p = getPrime(512)
io.sendlineafter(b">", b"2")
io.sendlineafter(b">", b"3")
io.sendlineafter(b">", str(p).encode())

n = int(io.recvline_startswith(b"n").split(b"=")[1])
e = int(io.recvline_startswith(b"e").split(b"=")[1])
ct = int(io.recvline_startswith(b"cipher").split(b"=")[1])

d = pow(e, -1, p - 1)
m = pow(ct, d, p)
print(long_to_bytes(m))
