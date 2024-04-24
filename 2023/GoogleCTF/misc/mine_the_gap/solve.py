from collections import defaultdict, deque
from copy import deepcopy


def solve(X, diff):
    def print_table(i, j, l):
        for ii in range(i - l, i + l + 1):
            for jj in range(j - l, j + l + 1):
                print(hex(X[ii][jj])[2:], end=" ")
            print()

    def fix(i, j, x):
        assert X[i][j] == 9
        X[i][j] = x
        print(i, j, x)
        if x == 11:
            for ni, nj in G[(i, j)]:
                G[ni, nj].remove((i, j))
                X[ni][nj] -= 1
                check_and_append(ni, nj)
        else:
            for ni, nj in G[(i, j)]:
                G[ni, nj].remove((i, j))
                check_and_append(ni, nj)

    def check_and_append(i, j):
        if X[i][j] == 0:
            # フラグを立てないことが確定している
            Q.append((i, j))
        elif len(G[i, j]) == X[i][j]:
            # フラグを立てることが確定している
            Q.append((i, j))

    def is_complete():
        h, w = len(X), len(X[0])
        ng = []
        for i in range(h):
            for j in range(w):
                if X[i][j] == 9:
                    ng.append((i, j))
        if ng:
            # print(len(ng), ng)
            return False
        return True

    h = len(X)
    w = len(X[0])
    G = defaultdict(list)

    for i, j, x in diff:
        assert X[i][j] == 9
        fix(i, j, x)

    # 数字 <-> 箱
    for i in range(h):
        for j in range(w):
            if X[i][j] == 0:
                continue
            if 0 < X[i][j] < 9:
                for di, dj in DIR:
                    ni, nj = i + di, j + dj
                    if X[ni][nj] == 9:
                        G[i, j].append((ni, nj))
                        G[ni, nj].append((i, j))
                    elif X[ni][nj] == 11:
                        X[i][j] -= 1

    Q = deque()
    for i, j in G.keys():
        check_and_append(i, j)

    while Q:
        i, j = Q.pop()
        if X[i][j] == 0:
            # フラグを立てないことが確定している箱たち
            S = [(ni, nj) for ni, nj in G[i, j]]
            for ni, nj in S:
                fix(ni, nj, 12)
        else:
            # フラグを立てることが確定している箱たち
            S = [(ni, nj) for ni, nj in G[i, j]]
            for ni, nj in S:
                fix(ni, nj, 11)

    return is_complete()


with open("gameboard.txt", "r") as fin:
    X = fin.read()
    X = X.replace(" ", "0")
    X = [[*map(lambda t: int(t, 16), line)] for line in X.split("\n") if len(line) > 0]


DIR = []
for di in [-1, 0, 1]:
    for dj in [-1, 0, 1]:
        if di == dj == 0:
            continue
        DIR.append((di, dj))

solve(X, [(23, 9, 11), (23, 9 + 24, 11)])
# solve(X, [(912, 9, 12)])
