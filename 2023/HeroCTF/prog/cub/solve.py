from collections import defaultdict
import pickle

with open('puzzle.pickle', 'rb') as p:
    P = pickle.load(p)

L = defaultdict(int)
R = defaultdict(int)
U = defaultdict(int)
D = defaultdict(int)

for i, p in enumerate(P):
    u, r, d, l, _ = p
    L[l] = i
    R[r] = i
    U[u] = i
    D[d] = i

i = 0
u, r, d, l, _ = P[i]

while l in R:
    i = R[l]
    u, r, d, l, _ = P[i]

while u in D:
    i = D[u]
    u, r, d, l, _ = P[i]

for _ in range(64):
    u, r, d, l, payload = P[i]
    print(payload, end='')
    i = L[r]
    u, r, d, l, _ = P[i]
    i = U[d]
    u, r, d, l, _ = P[i]
