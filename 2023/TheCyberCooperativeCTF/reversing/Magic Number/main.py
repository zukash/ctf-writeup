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


flag = 9873456
v = func1(flag)
v = func2(v, 4)
v = func1(v)
v = func2(v, 8)

if v == 0x96A878D249249:
    print("Correct")