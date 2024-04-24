import re
from pwn import *

io = remote('you-spin-me-round.knping.pl', '20000')
# io = process(['python', 'you-spin-me-round/src/main.py'])

def solve1(task):
    # Task 1: x // ? = z
    # ex) 6039 // ? = 83
    m = re.match(br'(\d+) // \? = (\d+) ', task)
    x, z = int(m.group(1)), int(m.group(2))
    return str(x // z)

def solve2(task):
    # Task 2: (x/100) % ? = (z/100)
    # ex) 1530461.15 % ? = 19.3399999998353 
    m = re.match(br'(\d+.\d+) % \? = (\d+.\d+) ', task)
    x, z = m.group(1), m.group(2)
    x, z = float(x), float(z)
    z_float = z
    x, z = int(round(x * 100)), int(round(z * 100))

    # x = b * (x // y) + (x % y)
    # x - (x % y) = b * (x // y)
    ans = []
    for b in divisors(x - z):
        q = (x - z) // b
        y = (x - z) // q
        if x % y == z:
            ans.append((abs(float(x/100) % float(y/100) - z_float), y))
    return str(float(min(ans)[1] / 100))

def solve3(task):
    # Task 3: 9098024.66 % 904.4 = ?
    m = re.match(br'(\d+.\d+) % (\d+.\d+) = ', task)
    x, z = m.group(1), m.group(2)
    x, z = float(x), float(z)

    return str(x % z) + '00000000001'


for _ in range(999):
    print(io.recvregex(br'Task \d+: '))
    task = io.readline()
    if b'// ?' in task:
        y = solve1(task)
    elif b'% ?' in task:
        y = solve2(task)
    elif b'= ?' in task:
        y = solve3(task)
    print(y)
    # io.interactive()
    io.sendlineafter(b'in the task above:', str(y).encode())

io.interactive()
# io.recvuntil(b'Task 1: ')
# task = io.readline()
# y = solve1(task)
# io.sendlineafter(b'in the task above:', str(y).encode())

# io.recvuntil(b'Task 2: ')
# task = io.readline()
# y = solve2(task)
# io.sendlineafter(b'in the task above:', str(float(y / 100)).encode())

# io.recvuntil(b'Task 3: ')
# task = io.readline()
# y = solve3(task)
# io.sendlineafter(b'in the task above:', y.encode())

# io.interactive()


# """
# 8615 1230
# b'2651913.78' b'96.63999999980925'
# 2651913.78 96.63999999980925
# 265191378 9664
# 1 265181714
# 265191378, 1, 9664, 0
# 2 132590857
# 265191378, 2, 9664, 0
# 7 37883102
# 265191378, 7, 9664, 4
# 14 18941551
# 265191378, 14, 9664, 4
# 1523 174118
# 265191378, 1523, 9664, 526
# 3046 87059
# 265191378, 3046, 9664, 526
# 10661 24874
# 265191378, 10661, 9664, 9664
# [*] Switching to interactive mode
 
#     INCORRECT
#     YOUR SOLUTION:      2651913.78 % 10661.0 = 7985.779999999795
#     CORRECT:            2651913.78 % 106.61 = 96.63999999980925
#     OPTIONAL:           None
# """