from pwn import *

io = remote('without-love-it-cannot-be-seen.knping.pl', '30001')

io.sendlineafter(b'>', ''.join([chr(i) for i in range(300, 400)]).encode())
# io.sendlineafter(b'>', b'aaaa')
print(io.recvrepeat())

io.interactive()