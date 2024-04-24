from pwn import *

exe = ELF('./bofww')
context.binary = exe.path


print(flat(1))

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *input_person + 79
        b *input_person + 206
        continue
    """)
elif args.REMOTE:
    io = remote("addr", 1337)


# io.sendlineafter(b'?', b'\x00' + b'A' * 0xf + b'\x00' + b'B' * 0xf)
# io.sendlineafter(b'?', b'100')
# print(io.recvline())
# print(io.recvline())
# print(io.recvline())
io.interactive()

