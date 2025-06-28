from pwn import *

exe = ELF('./bankrupst')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main
        continue
    """)
elif args.REMOTE:
    io = remote("addr", 1337)

io.interactive()
