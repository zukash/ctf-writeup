import random

n = 4000
print(n)
L = [random.randint(1, 10 ** 9) for _ in range(n)]
print(*L)
for u in range(1, n):
    print(u, u + 1)
