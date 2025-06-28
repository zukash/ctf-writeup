from collections import defaultdict
import itertools
from typing import Counter


def genHash(V):
    Hash = []
    for i in range(len(V)):
        Value = 0
        for j in range(len(V)):
            if j == i and j > 0:
                Value -= V[j - 1]
                Value += V[j] ^ V[j - 1]
            else:
                Value += V[j]
        Hash.append(Value)
    return Hash


def genHashMod(V):
    Hash = [sum(V)]
    for i in range(1, len(V)):
        Value = sum(V)
        Value += (V[i] ^ V[i - 1]) - V[i] - V[i - 1]
        Hash.append(Value)
    return Hash


def genAnotherHash(V):
    Hash = [sum(V)]
    for i in range(1, len(V)):
        # V[i] + V[i + 1] の繰り上がり場所が同じ
        # Hash.append((V[i] + V[i - 1]) - (V[i] ^ V[i - 1]))
        Hash.append(V[i] & V[i - 1])
    return Hash


"""
(68, 28, 36) [(21, 20, 27), (21, 22, 25), (21, 28, 19), (21, 30, 17), (22, 20, 26), (22, 28, 18), (23, 20, 25), (23, 28, 17), (29, 20, 19), (29, 22, 17), (30, 20, 18), (31, 20, 17)]
a + b + c == 68
a & b == 20
b & c == 16
(20, 20, 16) == (0b10100, 0b10100, 0b10000)
68 - 56 == 12

"""

n = 3
m = 5


P = list(itertools.product(*[range(pow(2, m))] * n))
for p in P:
    assert genHash(p) == genHashMod(p)


C = Counter()
for p in P:
    C[tuple(genHash(p))] += 1

D = Counter()
for p in P:
    D[tuple(genAnotherHash(p))] += 1

print(sorted(C.values()))
assert sorted(C.values()) == sorted(D.values())

E = defaultdict(list)
for p in P:
    E[tuple(genHash(p))].append(p)

for k, v in E.items():
    if len(v) > 1:
        print(k, v)
