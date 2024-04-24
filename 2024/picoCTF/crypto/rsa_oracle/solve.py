from pwn import *
from Crypto.Util.number import long_to_bytes

io = remote("titan.picoctf.net", "62026")


def decrypt(ct):
    io.sendlineafter(b"?", b"D")
    io.sendlineafter(b":", str(ct).encode())
    io.recvuntil(b"(c ^ d mod n):")
    pt = int(io.recvline(), 16)
    return pt


def encrypt(pt):
    io.sendlineafter(b"?", b"E")
    io.sendlineafter(b":", pt)
    io.recvuntil(b"(m ^ e mod n)")
    ct = int(io.recvline())
    return ct


n = decrypt(-1) + 1
e = 65537
assert encrypt(b"\x02") == pow(0x2, e, n)

# pow(2 * m, e, n) == pow(2, e, n) * pow(m, e, n) % n

password_ct = 873224563026311790736191809393138825971072101706285228102516279725246082824238887755080848591049817640245481028953722926586046994669540835757705139131212
password_pt = decrypt(password_ct * pow(2, e, n) % n) * pow(2, -1, n) % n
password_pt = long_to_bytes(password_pt)
print(password_pt)
# 92d53
assert encrypt(password_pt) == password_ct

io.interactive()


# openssl enc -d -aes-256-cbc -in secret.enc -pass pass:92d53
