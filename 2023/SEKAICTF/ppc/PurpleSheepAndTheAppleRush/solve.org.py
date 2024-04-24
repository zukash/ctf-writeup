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
    C0, C1 = [], []
    for v in G[u]:
        if v == p:
            continue
        C0.append(dfs(v, u, x))
        C1.append(dfs(v, u, L[u]))
    c0 = x + min(C0)
    c1 = 1 + L[u] + min(C1)
    if ans[u] is not None:
        c1 = min(c1, ans[u])
    return min(c0, c1)


ans = [None] * n
for u in argsort(L):
    ans[u] = dfs(u, -1, INF)

print(*ans)
