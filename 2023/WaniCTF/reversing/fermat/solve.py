# from pwn import *

# io = process('./a.out')

# print(io.recv())
# # io.recvuntil(b'>')
# # io.sendline(b'100')

# # io.recvuntil(b'>')
# # io.sendline(b'101')

# # io.recvuntil(b'>')
# # io.sendline(b'102')

# print(io.recvrepeat())

MOD = 4294967296
for a in range(1626, 3000):
    for b in range(1626, 3000):
        for c in range(1626, 3000):
            if (a ** 3 + b ** 3) % MOD == (c ** 3) % MOD:
                print(a, b, c)