from pwn import *
from Crypto.Util.number import *

"""
given:
1. AES_CBC(RSA(x))
2. RSA_inv(AES_CBC_inv(x))
3. RSA(flag)

approach:
AES_CBC を自作する。
AES_ECB が作れれば良い。

RSA(x) で任意のブロックを作れるか。
↓
AES_CBC_inv(x) で任意ブロックが作れるので、
RSA(RSA_inv(AES_CBC_inv(x))) で任意のブロックが作れる。
"""

io = process(["python", "server.mod.py"])
# io = remote("ares.beginners.seccon.games", 5000)

# context.log_level = "debug"


def to_hex(x):
    return f"{x:032x}"


def xor_hex(h0, h1):
    return to_hex(int(h0, 16) ^ int(h1, 16))


def CBC_RSA(x):
    io.sendlineafter(b"> ", b"1")
    io.sendlineafter(b"m: ", str(x).encode())
    io.recvuntil(b"c: ")
    iv_ct = io.recvline().strip().decode()
    iv, ct = iv_ct[:32], iv_ct[32:]
    return iv, ct


def RSA_inv_CBC_inv(iv, ct):
    io.sendlineafter(b"> ", b"2")
    io.sendlineafter(b"c: ", (iv + ct).encode())
    io.recvuntil(b"m: ")
    return int(io.recvline().strip())


def ECB_decode(block):
    block_ci_ri = RSA_inv_CBC_inv("00" * 16, block)
    return to_hex(pow(block_ci_ri, e, n))


def CBC_encode(pt):
    assert len(pt) % 32 == 0
    ct = cb = "00" * 16
    for i in range(0, len(pt), 32)[::-1]:
        pb = pt[i : i + 32]
        pb_xor_ncb = ECB_decode(cb)
        cb = xor_hex(pb, pb_xor_ncb)
        ct = cb + ct
    iv, ct = ct[:32], ct[32:]
    return iv, ct


def RSA_inv(x):
    x_ci_ri = RSA_inv_CBC_inv("00" * 16, to_hex(x))
    x_ci = pow(x_ci_ri, e, n)
    return RSA_inv_CBC_inv(to_hex(x ^ x_ci), to_hex(x))


io.recvuntil(b"enc_flag: ")
flag_r = io.recvline().strip().decode()

e = 65537
n = RSA_inv_CBC_inv(*CBC_RSA(-1)) + 1
print(f"{n = }")

# print(CBC_RSA("00" * 32))
iv, ct = CBC_encode(flag_r)
m = RSA_inv_CBC_inv(iv, ct)
print(long_to_bytes(m))

io.interactive()
