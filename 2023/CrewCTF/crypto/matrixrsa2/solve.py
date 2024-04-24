from Crypto.Util.number import *
from pwn import *


def to_hex(x):
    hx = hex(x)[2:]
    if len(hx) & 1:
        hx = "0" + hx
    if len(hx) == 0:
        hx = "00"
    return hx


class Oracle:
    def send(self, ea, em):
        io.recvuntil(b">>")
        io.sendline(to_hex(ea).encode())
        io.recvuntil(b">>")
        io.sendline(to_hex(em).encode())

    def recv(self):
        res = io.recvline()
        if b"size error" in res:
            return None
        return io.recvline().decode().strip()


count = 0
while True:
    count += 1
    print(count)
    io = process(["sage", "server.mod.sage"])
    # io = remote("matrixrsa2.chal.crewc.tf", "20002")
    oracle = Oracle()

    # recv enc
    io.recvuntil(b"Here is encrypted flag(enc_0, enc_1):")
    io.recvline()
    enc0 = io.recvline().decode().strip()
    enc1 = io.recvline().decode().strip()

    # send 0
    ea = int(enc0, 16)
    em = int(enc1, 16) * 2
    oracle.send(ea, em)

    # recv 0
    res = oracle.recv()
    if res is None:
        io.close()
        continue
    flag2 = int(res, 16)

    io.recvuntil(b"Please input encrypted message(enc_0, enc_1):")

    # send 1
    ea = int(enc0, 16)
    em = 0
    oracle.send(ea, em)

    # recv 1
    res = oracle.recv()
    if res is None:
        io.close()
        continue
    alpha = int(res, 16)
    # print(hex(alpha), file=sys.stderr)

    flag = long_to_bytes((flag2 + alpha) // 2)

    print(flag)
    if b"crew" in flag:
        print(flag)
        print(count)
        break

    io.close()
