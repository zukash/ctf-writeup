from pwn import *
from tqdm import trange

INF = 10**18
io = remote("krusty-katering.ctf.umasscybersec.org", 1337)


def parse_time_to_int(t):
    m = 0
    if b"m" in t:
        m, t = t.split(b"m")
        m = int(m)
    s = 0
    if b"s" in t:
        s, t = t.split(b"s")
        s = int(s)
    return m * 60 + s


def assign_job(t):
    i = T.index(min(T))
    T[i] += t
    return i


for _ in range(5):
    T = [INF] + [0] * 10
    for _ in trange(1000):
        # io.recvuntil(b"Price: $")
        # price = float(io.recvline())
        io.recvuntil(b"cook:")
        time = parse_time_to_int(io.recvline())

        cook = assign_job(time)
        io.sendline(str(cook).encode())

io.interactive()
