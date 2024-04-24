"""
ずっと先の未来を予測したい
ダブリング的なことができないか
行列で表せば、行列累乗ができる
"""
from secret import flag, seed

n = 128
AA = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if j == i + 1:
            AA[i][j] = 1

AA[n - 1][0] = 1
AA[n - 1][2] = 1
AA[n - 1][4] = 1
AA[n - 1][6] = 1
AA[n - 1][9] = 1
AA = matrix(Zmod(2), AA)

BB = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if j == i + 1:
            BB[i][j] = 1

BB[n - 1][1] = 1
BB[n - 1][5] = 1
BB[n - 1][7] = 1
BB[n - 1][8] = 1
BB = matrix(Zmod(2), BB)


def get_seed(R):
    return sum([int(r) << i for i, r in enumerate(R)])


# 内部状態R　初めはS (seed)
R = S = vector(Zmod(2), [seed >> i & 1 for i in range(n)])
assert seed == get_seed(R)

CC = BB * AA
neko = ord("🐈") * ord("🐈") * ord("🐈")

# nekoの後のR
R = (CC ** (neko * 8 // 2)) * R
print(get_seed(R))

# 続きは problem.mod.py で
