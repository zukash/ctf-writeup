from pwn import *
from tqdm import trange

io = remote("34.134.200.24", "31227")

# mic test >  v [1/100]
for _ in trange(100):
    m = io.recvregex(rb"mic test >  (.*) \[", capture=True)
    io.sendline(m.group(1))

io.interactive()
