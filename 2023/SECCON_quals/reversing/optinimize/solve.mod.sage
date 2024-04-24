import tqdm


def solve(x):
    M = matrix(Zmod(x), [[0, 1, 1], [1, 0, 0], [0, 1, 0]])
    return M ** x * vector([2, 0, 3])


Q = []
for x in tqdm.trange(10 ** 4):
    Q.append(solve(x))

print(Q)
print([i for i, q in enumerate(Q) if q == 0])
