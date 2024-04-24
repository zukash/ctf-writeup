from base64 import *
from pwn import *
from itertools import product

# context.log_level = "debug"
io = remote("tamuctf.com", 443, ssl=True, sni="criminal")
# io = process(["python3", "server.py"])

flag = "gigem{"
while flag[-1] != "}":
    mn = (10**18, "")
    for c in "abcdefghijklmnopqrstuvwxyz_{}":
        io.sendlineafter(b"flag:", (flag + c).encode())
        res = b64decode(io.recvline().strip())
        mn = min(mn, (len(res), c))
        print(flag + c, len(res))
    flag += mn[1]

print(flag)
