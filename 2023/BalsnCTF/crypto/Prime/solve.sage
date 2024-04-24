from pwn import *

io = process(["sage", "chall.sage"])

k = prod(primes(100))
bit = 256 - k.bit_length()
for i in range(1 << (bit // 3), 1 << 512):
    p, q, r = 6 * (k * i) + 1, 12 * (k * i) + 1, 18 * (k * i) + 1
    if is_prime(p) and is_prime(q) and is_prime(r):
        n = p * q * r
        if 256 <= n.bit_length() <= 512:
            break

io.sendlineafter("prime: ", str(n).encode())
io.sendlineafter("factor: ", str(p).encode())
io.interactive()
