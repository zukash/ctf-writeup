from collections import defaultdict
import pickle

with open('puzzle.pickle', 'rb') as p:
    P = pickle.load(p)

L = defaultdict(int)
R = defaultdict(int)
U = defaultdict(int)
D = defaultdict(int)
F = defaultdict(int)
B = defaultdict(int)

for i, p in enumerate(P):
    u, r, f, d, l, b, _ = p
    L[l] = i
    R[r] = i
    U[u] = i
    D[d] = i
    F[f] = i
    B[b] = i

i = 0
u, r, f, d, l, b, _ = P[i]

while l in R:
    i = R[l]
    u, r, f, d, l, b, _ = P[i]

while u in D:
    i = D[u]
    u, r, f, d, l, b, _ = P[i]

while f in B:
    i = B[f]
    u, r, f, d, l, b, _ = P[i]

for _ in range(32):
    u, r, f, d, l, b, payload = P[i]
    print(payload, end='')
    i = L[r]
    u, r, f, d, l, b, _ = P[i]
    i = U[d]
    u, r, f, d, l, b, _ = P[i]
    i = F[b]
    u, r, f, d, l, b, _ = P[i]
