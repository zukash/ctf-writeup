from pwn import *

io = process(["python", "challenge.py"])


def get_hint():
    io.sendlineafter(b">", b"1")
    return io.recvline_contains(b"hint:").split(b": ")[1].strip()


H = [set() for _ in range(15)]
for _ in range(100):
    hint = get_hint()
    for i, c in enumerate(hint):
        H[i].add(c)

S = set(hint)
magic_word = "".join([chr((S - H[i]).pop()) for i in range(15)])

io.sendlineafter(b">", b"2")
io.sendline(magic_word.encode())
io.interactive()
