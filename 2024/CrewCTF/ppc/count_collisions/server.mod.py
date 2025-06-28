import secrets
import itertools
from collections import Counter

FLAG = "fakeflag"


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


n = 3
m = 5

"""
I swear in my computer this runs very fast
Trust me
"""


def cntcollisions(Hsh):
    P = itertools.product(*[range(pow(2, m))] * n)
    cnt = 0
    C = Counter()
    for a in P:
        cnt += genHash(a) == Hsh
        C[tuple(genHash(a))] += 1
    print(C)
    return cnt


print("I bet you can't count the number of collisions of this Hash!")

for T in range(10):
    print("How many collisions?:")
    msg = [secrets.randbelow(pow(2, m)) for i in range(n)]
    Hash = genHash(msg)
    print(Hash)

    cntUser = int(input())

    if cntcollisions(Hash) == cntUser:
        print("Correct!")
    else:
        print("Nope!")
        exit(0)

print("You found a flag!")
print(FLAG)
