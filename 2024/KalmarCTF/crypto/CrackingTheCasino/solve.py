from pwn import *
from randcrack import RandCrack
from tqdm import trange

# io = process(["python", "casino.py"])
io = remote("chal-kalmarc.tf", 9)

io.recvuntil(b"q = ")
q = int(io.recvline())
io.recvuntil(b"g = ")
g = int(io.recvline())
io.recvuntil(b"h = ")
h = int(io.recvline())
io.sendlineafter(b"?", b"x")

RC = RandCrack()
for _ in trange(624):
    io.recvuntil(b"Commitment:")
    c = int(io.recvline())
    io.sendlineafter(b"?", b"n")
    io.recvuntil(b"commited value was")
    x = int(io.recvline())
    io.recvuntil(b"randomness used was")
    r = int(io.recvline())
    assert c == (pow(g, x, q) * pow(h, r, q)) % q
    RC.submit(x)

for _ in range(100):
    io.sendlineafter(b"?", b"y")
    x = RC.predict_randint(0, 2**32 - 2)
    io.sendlineafter(b"?", str(x).encode())

io.interactive()

"""
Oh wow! well done!
Oh wow, you broke my casino??!? Thanks so much for finding this before launch so i don't lose all my money to cheaters!
here's that flag you wanted, you earned it! Kalmar{First_Crypto_Down!}
"""
