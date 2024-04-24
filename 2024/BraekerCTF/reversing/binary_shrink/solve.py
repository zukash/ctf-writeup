from pwn import *

context.binary = './binary_shrink'
code = """
"""

print(asm(code))
print(len(asm(code)))


# io = process('./binary_shrink')
io = gdb.debug('./binary_shrink', """
    b *main
    """)

io.interactive()

