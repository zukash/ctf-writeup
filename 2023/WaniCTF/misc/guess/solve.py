from collections import Counter
from pwn import *


class Oracle:
    def peep(self, L):
        io.recvuntil(b'>')
        io.sendline(b'1')
        io.recvuntil(b'>')
        message = " ".join(map(str, L))
        io.sendline(message.encode())
        res = io.recvline().decode()
        res = res[2:-2].split(',')
        res = list(map(int, res))
        return res
    
    def guess(self, L):
        io.recvuntil(b'>')
        io.sendline(b'2')
        io.recvuntil(b'>')
        message = " ".join(map(str, L))
        io.sendline(message.encode())


n = 10000
STEP = 10
SIZE = n // STEP
io = remote('guess-mis.wanictf.org', 50018)
# io = process('python', './chall.py')
oracle = Oracle()

ans = []
for r in range(STEP):
    L = []
    for i in range(SIZE):
        L += [i + r * SIZE] * (i + 1)
    res = oracle.peep(L)
    res = Counter(res).items()
    res = sorted(res, key=lambda t: t[1])
    ans += [k for k, v in res]
    print(f'Done: {r}')

# print(ans)
# print(len(ans))
oracle.guess(ans)
io.interactive()