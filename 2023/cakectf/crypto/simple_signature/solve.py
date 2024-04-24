from pwn import *
from hashlib import sha512

io = remote('crypto.2023.cakectf.com', '10444')

def verify(m, sig, key):
    w, v = key
    s, t = sig

    return pow(g, m, p) == pow(s, w, p) * pow(t, -v, p) % p

def h(m):
    return int(sha512(m.encode()).hexdigest(), 16)

magic_word = "cake_does_not_eat_cat"


p = None
exec(io.recvline())
g = None
exec(io.recvline())
vkey = None
exec(io.recvline())
w, v = vkey

target = pow(g, h(magic_word), p)

print(f'{p = }')
print(f'{g = }')
print(f'{w = }')
print(f'{v = }')
print(f'{h(magic_word) = }')
print(f'{target = }')

t = 2
sw = target * pow(t, v, p) % p
s = pow(sw, pow(w, -1, p - 1), p)
assert sw * pow(t, -v, p) % p == target
assert pow(s, w, p) * pow(t, -v, p) % p == target

io.recvuntil(b':')
io.sendline(b'V')
io.recvuntil(b':')
io.sendline(magic_word.encode())
io.recvuntil(b':')
io.sendline(str(s).encode())
io.recvuntil(b':')
io.sendline(str(t).encode())

io.interactive()
