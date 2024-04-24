INF = 10 ** 18


def bfs(edges, s):
    dist = [INF] * len(edges)
    dist[s] = 0
    que = [s]
    for u in que:
        for v in edges[u]:
            if dist[v] != INF:
                continue
            dist[v] = dist[u] + 1
            que.append(v)
    return dist


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    G = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        G[u].append(v)
    s, t = map(int, input().split())
    D = bfs(G, s)
    if D[t] <= 6:
        print("YES")
    else:
        print("NO")

"""
2
7 6
0 1
1 2
2 3
3 4
4 5
5 6
0 6
10 7
0 1
1 0
0 2
0 4
1 8
8 1
9 8
0 9
"""
