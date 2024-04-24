from pwn import *

# io = process('./aplet321')
io = remote('chall.lac.tf', '31321')

payload = b''

payload += b'pretty ' * 15
payload += b'please ' * 39
payload += b'flag'

io.sendline(payload)
io.interactive()