import re
import sys
from collections import defaultdict
from typing import Counter

from tqdm import tqdm

sys.setrecursionlimit(10 ** 8)


def convolve(f, g):
    h = [0] * (len(f) + len(g))
    for i in range(len(f)):
        for j in range(len(g)):
            h[i + j] += f[i] * g[j]
    return h


def comb(n, k):
    ans = 1
    for i in range(1, k + 1):
        ans *= n - i + 1
        ans //= i
    return ans


# word_list の読み取り
def get_word_list():
    with open("USACONST.TXT", encoding="ISO8859") as f:
        text = f.read()
    return list(set(re.sub("[^a-z]", " ", text.lower()).split()))


WW = get_word_list()
WW = sorted(WW, key=lambda t: len(t))
PP = []
for W in WW:
    for i in range(len(W) - 1):
        PP.append(W[:i])
print(len(WW))
print(len(PP))
f = [1]
for k, v in Counter([len(W) for W in WW]).items():
    g = [0] * (k * v + 1)
    for i in range(0, k * v + 1, k):
        g[i] = comb(v, i // k)
    f = convolve(f, g)[:30]
print(f)


# ヒントの読み取り
with open("hint.dot", "r") as f:
    lines = f.read().strip().split("\n")

lines = lines[1:-1]
nodes = {}
edges = []
for line in lines:
    if "label" in line:
        nid, label = re.findall(r"(\d+) \[label=(.+)\]", line.strip())[0]
        nodes[int(nid)] = label
        # nodes.append((int(nid), label))
    else:
        u, v = line.replace(";", "").strip().split(" -- ")
        edges.append((int(u), int(v)))

# 無向グラフの構築
n = len(nodes)
G = defaultdict(list)
for u, v in edges:
    G[u].append(v)
    G[v].append(u)

# dfsでpassphraseの候補を絞る
def dfs(u):
    print(path)
    for v in G[u]:
        if V[v]:
            continue

        path[-1] += nodes[v]
        V[v] = 1

        if path[-1] not in PP:
            continue
        if path[-1] in WW:
            path.append([])

        dfs(v)

        path[-1] = path[-1][:-1]
        V[v] = 0
        if len(path[-1]) == 0:
            path.pop()


U = defaultdict(lambda: 0)
V = defaultdict(lambda: 0)
path = [[]]
ANS = []
length = 0
C = Counter()
X = Counter(nodes.values())
print(X)
X_len = sum(X.values())
for u in nodes.keys():
    dfs(u)
print(ANS)
print(WW[0])

# 候補を全て試す
