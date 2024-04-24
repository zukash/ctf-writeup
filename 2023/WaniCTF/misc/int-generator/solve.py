import random

k = 36
maxlength = 16


def f(x, cnt):
    cnt += 1
    r = 2**k
    if x == 0 or x == r:
        return -x, cnt
    if x * x % r != 0:
        return -x, cnt
    else:
        return -x * (x - r) // r, cnt


def g(x):
    ret = x * 2 + x // 3 * 10 - x // 5 * 10 + x // 7 * 10
    ret = ret - ret % 2 + 1
    return ret, x // 100 % 100


def digit(x):
    cnt = 0
    while x > 0:
        cnt += 1
        x //= 10
    return cnt


def pad(x, cnt):
    minus = False
    if x < 0:
        minus = True
        x, cnt = g(-x)
        # print(f'{x=}, {cnt=}')
    sub = maxlength - digit(x)
    ret = x
    for i in range(sub - digit(cnt)):
        ret *= 10
        if minus:
            ret += pow(x % 10, x % 10 * i, 10)
        else:
            ret += pow(i % 10 - i % 2, i % 10 - i % 2 + 1, 10)
    # print(f'{ret=}')
    ret += cnt * 10 ** (maxlength - digit(cnt))
    # print(f'{ret=}')

    return ret


def int_generator(x):
    ret = -x
    x_, cnt = f(x, 0)
    while x_ > 0:
        ret = x_
        x_, cnt = f(x_, cnt)
    # print(f'{x=}, {ret=}, {cnt=}')
    return pad(ret, cnt)







S = [1008844668800884, 2264663430088446, 6772814078400884]

k = 36
r = 2**k

x = 0
while (x * 2 ** (k//2)) < 2 ** k:
    if int_generator(x * 2 ** (k//2)) in S:
        print(x * 2 ** (k//2))
        print(S.index(int_generator(x * 2 ** (k//2))))
    x += 1

# print(int_generator(-4772814078400884))

"""
2 ** 16 * a + b
2 ** 16 * b + a
2 ** 32 * (a * b)


a0b0c0d0
0x0y0z0w
"""