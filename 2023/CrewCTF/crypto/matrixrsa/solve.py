from Crypto.Util.number import *
from pwn import *


while True:
    # io = process(["sage", "server.mod.sage"])
    io = remote("matrixrsa.chal.crewc.tf", "20001")

    # recv
    io.recvuntil(b"Here is encrypted flag(enc_0, enc_1):")
    io.recvline()
    enc0 = io.recvline().decode().strip()
    enc1 = io.recvline().decode().strip()

    # send
    ea = int(enc0, 16)
    em = int(enc1, 16) * 2
    io.recvuntil(b">>")
    io.sendline(hex(ea)[2:].encode())
    io.recvuntil(b">>")
    io.sendline(hex(em)[2:].encode())

    # check
    res = io.recvline()
    if b"size error" in res:
        continue
    ans = io.recvline().decode().strip()
    ans = int(ans, 16) // 2
    flag = long_to_bytes(ans)
    if b"crew" in flag:
        print(flag)
        exit()
    io.close()
