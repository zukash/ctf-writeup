from pwn import *

# nc challs.actf.co 31300
io = remote("challs.actf.co", "31300")

for i in range(64):
    print(f"============ {i} ============")
    io.recvuntil(b"pubkey:")
    pk = int(io.recvline())

    io.recvuntil(b"plaintext:")
    pt = int(io.recvline())

    secret = (pt**2 % pk) ^ (1 / 2)
    print(f"{int(secret):032x}")
    io.sendlineafter(b"gimme the secret: ", f"{int(secret):032x}".encode())
io.interactive()
