import re
from pwn import *
from tqdm import trange

io = remote('you-spin-me-round.knping.pl', '20000')
# io = process(['python', 'you-spin-me-round/src/main.py'])

def solve1(task):
    # Task 1: x // ? = z
    # ex) 6039 // ? = 83
    m = re.match(br'(\d+) // \? = (\d+) ', task)
    x, z = int(m.group(1)), int(m.group(2))

    S.append(x)
    S.append(x // z)
    return str(x // z)

def solve2(task):
    # Task 2: (x/100) % ? = (z/100)
    # ex) 1530461.15 % ? = 19.3399999998353 
    m = re.match(br'(\d+.\d+) % \? = ([^ ]+) ', task)
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

    S.append(x)
    S.append(min(ans)[1])
    return str(float(min(ans)[1] / 100))

def solve3(task):
    # Task 3: 9098024.66 % 904.4 = ?
    m = re.match(br'(\d+.\d+) % ([^ ]+) = ', task)
    x, z = m.group(1), m.group(2)
    x, z = float(x), float(z)

    return str(x % z) + '00000000001'


S = []

header = io.recvuntil(b'PLEASE ENTER CORRECT SOLUTIONS TO AUTHORIZE:')
beep, boop = header.count(b'BEEP'), header.count(b'BOOP')
S.append(beep)
S.append(boop)

for _ in range(2):
    io.recvregex(br'Task \d+: ')
    task = io.readline()
    if b'// ?' in task:
        y = solve1(task)
    elif b'% ?' in task:
        y = solve2(task)
    elif b'= ?' in task:
        y = solve3(task)
    io.sendlineafter(b'in the task above:', str(y).encode())

with open('out.out') as f:
    db = f.readlines()

seed = db.index(str(S) + '\n')

ans = []

def task1():
    x = random.randint(100, 10000)
    y = random.randint(1, 100)
    ans.append(str(y))

def task2():
    x = random.randint(100000, 1000000000) / 100
    y = random.randint(1, 100000) / 100
    ans.append(str(float(y)))


def task3():
    x = random.randint(100000, 1000000000) / 100
    y = random.randint(1, 100000) / 100
    ans.append(str(float(float(x) % float(y))) + '000000000000000000000000001')

def task4():
    for i in range(4, 1_000):
        task = random.randint(1, 3)
        eval(f'task{task}()')

random.seed(seed)
random.randint(1, 100)
random.randint(1, 100)
task1()
task2()
task3()
task4()
# print(seed)
# print('\n'.join(ans))


io.sendline('\n'.join(ans[2:]).encode())
io.interactive()
