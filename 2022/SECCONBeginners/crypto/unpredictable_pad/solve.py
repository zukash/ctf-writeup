from pwn import *
from Crypto.Util.number import long_to_bytes
from randcrack import RandCrack


io = process(["python", "chal.py"])

inp = ~(1 << (623 * 32))
io.sendlineafter(b"oracle:", str(inp).encode())
io.recvuntil(b"The oracle is:")
orcale = int(io.recvline())
r = orcale ^ inp

X = []
for i in range(624):
    x = r & ((1 << 32) - 1)
    X.append(x)
    r >>= 32

print(X)

rc = RandCrack()
for x in X:
    rc.submit(x)

flag_bit = 223
inp = ~(1 << flag_bit)
io.sendlineafter(b"oracle:", str(inp).encode())
io.sendlineafter(b"oracle:", str(inp).encode())

io.recvuntil(b"Encrypted flag: ")
oracle = int(io.recvline())

rc.predict_getrandbits(flag_bit)
rc.predict_getrandbits(flag_bit)
r = rc.predict_getrandbits(flag_bit)

pt = oracle ^ r
print(long_to_bytes(pt))

io.interactive()
