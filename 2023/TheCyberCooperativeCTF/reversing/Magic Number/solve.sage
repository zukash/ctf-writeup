from Crypto.Util.number import *

def func1(v):
    return v + 0x11 * 4


def func2(v1, v2):
    if v1 == 1 or not v2:
        return v1
    if v1 & 1 == 0:
        return func2(v1 >> 1, v2 - 1)
    v3 = func3(v1, 3)
    return func2(v3 + 1, v2 - 1)


def func3(v1, v2):
    for _ in range(v2):
        v1 *= 2
    return v1


def naive(flag):
    v = func1(flag)
    v = func2(v, 4)
    v = func1(v)
    v = func2(v, 8)
    return v

####################################


def f1(v):
    return v + 0x44


def f2(v1, v2):
    while v1 != 1 and v2 != 0:
        if v1 & 1 == 0:
            # v1 偶数
            v1 //= 2
            v2 -= 1
        else:
            # v1 奇数
            v1 = v1 * 8 + 1
            v2 -= 1
    return v1


# def f3(v1, v2):
#     return v1 << v2


def convert(flag):
    v = f1(flag)
    v = f2(v, 4)
    v = f1(v)
    v = f2(v, 8)
    return v

#####################################


# for i in range(10**5):
#     assert naive(i) == convert(i)


#####################################

for bit in range(1 << 12):
    x = var('x')
    f = x
    # v = f1(flag)
    f += 0x44

    # v = f2(v, 4)
    for i in range(4):
        if bit >> i & 1:
            f = f * 8 + 1
        else:
            f /= 2
    
    # v = f1(v)
    f += 0x44

    # v = f2(v, 8)
    for i in range(8):
        if bit >> (i + 4) & 1:
            f = f * 8 + 1
        else:
            f /= 2

    # print(f == 0x96A878D249249)
    ans = solve(f == 0x96A878D249249, x)[0].rhs()
    if ans.is_integer() and naive(int(ans)) == 0x96A878D249249:
        print(long_to_bytes(int(ans)))
        print(ans)


