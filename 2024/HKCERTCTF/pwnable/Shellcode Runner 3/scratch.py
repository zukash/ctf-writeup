from pwn import *

# run_assembly_exitcode('mov ebx, 3; mov eax, SYS_exit; int 0x80;')

# context.binary = "./src/chall"

# code = """
# xor eax, eax
# push eax

# push '//sh'
# push '/bin'

# mov ebx, esp
# """

print(shellcraft.i386.linux.sh())
io = run_assembly(shellcraft.i386.linux.sh())
io.interactive()
# run_assembly_exitcode(code)