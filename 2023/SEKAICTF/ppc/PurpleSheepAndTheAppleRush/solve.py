import sys

sys.setrecursionlimit(10 ** 8)


def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)


INF = 10 ** 18
n = int(input())
L = [*map(int, input().split())]
UV = [[*map(int, input().split())] for _ in range(n - 1)]

G = [[] for _ in range(n)]
D = [0] * n
for u, v in UV:
    u, v = u - 1, v - 1
    G[u].append(v)
    G[v].append(u)
    D[u] += 1
    D[v] += 1


def dfs(u, p, x):
    if D[u] == 1:
        return -L[u]
    if ans[u] is not None and L[u] < x:
        return ans[u]
    C = []
    for v in G[u]:
        if v == p:
            continue
        C.append(dfs(v, u, x))
    res = x + min(C)
    return res


ans = [None] * n
for u in argsort(L):
    if D[u] == 1:
        ans[u] = -L[u]
    else:
        ans[u] = dfs(u, -1, L[u]) + 1

print(*ans)
