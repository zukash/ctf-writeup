from pwn import *
from randcrack import RandCrack
from tqdm import trange


# io = process(['python', 'server.py'])
io = remote('0.cloud.chals.io', '30309')

"""
# 2181042827

=> 8 4 2
=> 1 0 8
=> 2 1 2
MULTIPLIER=7
"""

def check(f1, f2, f3):
    if f1[0] == f1[1] == f1[2]:
        return True, f1[0] + f1[1] + f1[2]

    if f2[0] == f2[1] == f2[2]:
        return True, f2[0] + f2[1] + f2[2]

    if f3[0] == f3[1] == f3[2]:
        return True, f3[0] + f3[1] + f3[2]

    if f1[0] == f2[1] == f3[2]:
        return True, f1[0] + f2[1] + f3[2]

    if f1[2] == f2[1] == f3[0]:
        return True, f1[2] + f2[1] + f3[0]

    return False, "###"

def sample():
    io.sendlineafter(b'WAGER?', b'1')
    M = []
    io.recvuntil(b'=>')
    M.append(io.recvline().split())
    io.recvuntil(b'=>')
    M.append(io.recvline().split())
    io.recvuntil(b'=>')
    M.append(io.recvline().split())
    # print(M)
    io.recvuntil(b'MULTIPLIER=')
    m = io.recvline().strip()
    # print(m)
    res = b""
    res += M[2][0] + M[1][0] + M[0][0]
    res += M[2][1] + M[1][1] + M[0][1]
    res += M[2][2] + M[1][2] + M[0][2]
    res += m
    return int(res)

def next_predict(rc):
    start = str(rc.predict_getrandbits(32))
    start = start.zfill(10)
    print(f'{start = }')

    r1 = start[0:3]
    r2 = start[3:6]
    r3 = start[6:9]
    multi = start[9]

    if multi == '0':
        return False

    f1 = r1[2] + r2[2] + r3[2]
    f2 = r1[1] + r2[1] + r3[1]
    f3 = r1[0] + r2[0] + r3[0]

    return check(f1, f2, f3)[0]


rc = RandCrack()
for _ in trange(624):
    rc.submit(sample())

while True:
    io.recvuntil(b'YOU HAVE')
    money = int(io.recvline().replace(b'MONEY', b''))
    if money >= 1000000:
        break

    print(f'{money = }')
    if next_predict(rc):
        print("WIN")
        io.sendlineafter(b'WAGER?', str(money).encode())
    else:
        print("LOSE")
        io.sendlineafter(b'WAGER?', b'1')
    # io.interactive()

io.interactive()