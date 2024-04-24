from pwn import *

io = remote('crypto.2023.cakectf.com', '10555')
# io = process(['sage', 'server.sage'])

io.recvuntil(b'Here is p:')
p = int(io.recvuntil(b',')[:-1])
assert is_prime(p)

io.recvuntil(b'and M:')
M = eval(io.recvuntil(b']'))
M = Matrix(GF(p), 5, 5, M)


period = multiplicative_order(det(M ** 3))

for x in range(1, 100):
    m = multiplicative_order(det(M ** x))
    if period % m == 0:
        print(x)


for _ in range(100):
    io.recvuntil(b'my commitment is=')
    commit = eval(io.recvuntil(b']'))
    commit = Matrix(GF(p), 5, 5, commit)
    for hand in range(1, 4):
        m = multiplicative_order(det(commit * (M ** hand)))
        print(hand, period % m)

    for hand in range(1, 4):
        m = multiplicative_order(det(commit * (M ** hand)))
        if period % m == 0:
            break

    if hand == 1:
        # 相手が Paper
        # 自分は Scissors
        hand = 2
    elif hand == 2:
        # 相手が Scissors
        # 自分は Rock
        hand = 1
    else:
        # 相手が Rock
        # 自分は Paper
        hand = 3

    io.recvuntil(b'your hand(1-3):')
    io.sendline(str(hand).encode())

    print(io.recvline())

io.interactive()

"""
1: Paper
2: Scissors
3: Rock

---
1: "Rock",
2: "Scissors",
3: "Paper"
"""