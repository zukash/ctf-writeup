from pwn import *
from Crypto.Util.number import *
from base64 import b64encode, b64decode


io = remote("rsa101.sstf.site", "1104")

m = bytes_to_long(b"cat flag")
m0 = 42073337
m1 = 170205956447
assert m0 * m1 == m

b0 = b64encode(long_to_bytes(m0))
b1 = b64encode(long_to_bytes(m1))

io.recvuntil(b"n = ")
n = int(io.recvline(), 16)
io.recvuntil(b"e = ")
e = int(io.recvline(), 16)

io.recvuntil(b">")
io.sendline(b"2")
io.recvuntil(b":")
io.sendline(b0)
io.recvuntil(b" Signed command:")
s0 = io.recvline()
c0 = bytes_to_long(b64decode(s0))

io.recvuntil(b">")
io.sendline(b"2")
io.recvuntil(b":")
io.sendline(b1)
io.recvuntil(b" Signed command:")
s1 = io.recvline()
c1 = bytes_to_long(b64decode(s1))

c = c0 * c1 % n
io.recvuntil(b">")
io.sendline(b"1")
io.recvuntil(b":")
io.sendline(b64encode(long_to_bytes(c)))

io.interactive()
