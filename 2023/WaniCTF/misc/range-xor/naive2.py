from  collections import defaultdict
A = [*map(int, input().split())]
n = len(A)

def f(x):
    return min(x, 1000 - x)

S = set()
for bit in range(1 << n):
    B = []
    ok = True
    for i in range(n):
        if bit >> i & 1:
            if f(A[i]) == A[i]:
                ok = False
            B.append(f(A[i]))
        else:
            B.append(A[i])
    if ok:
        S.add(tuple(B))

D = defaultdict(int)
for B in S:
    xor = 0
    for b in B:
        xor ^= b
    D[xor] += 1

print(sorted(D.items()))
# print(sorted(D.items())[0])


"""
532 746 606 601 293 825 912 826 789 190
"""