from pwn import *
from Crypto.Util.Padding import *
from functools import reduce

io = process(["python", "chal.py"])

io.sendlineafter(b">", b"1")
io.sendlineafter(b">", b"primes")

iv_enc = io.recvline_contains(b":").split(b":")[1].strip().decode()
iv, enc = iv_enc[:32], iv_enc[32:]
iv, enc = map(bytes.fromhex, [iv, enc])

new_iv = reduce(xor, [pad(b"primes", 16), iv, pad(b"getflag", 16)])
iv_enc = new_iv.hex() + enc.hex()

io.sendlineafter(b">", b"2")
io.sendlineafter(b">", iv_enc.encode())

io.interactive()
