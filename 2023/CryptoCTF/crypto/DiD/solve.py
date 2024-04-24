from pwn import *


def isqrt(n):
    ok = 0
    ng = n + 1
    while ng - ok > 1:
        x = (ok + ng) // 2
        if x ** 2 <= n:
            ok = x
        else:
            ng = x
    return ok


class Oracle:
    def send(self, L):
        io.sendline(",".join(map(str, L)).encode())
        io.recvuntil(b"=")
        res = io.recvline().decode()
        res = res.strip()[1:-1].split(",")
        res = list(map(int, res))
        return res

    def answer(self, L):
        io.sendline(",".join(map(str, L)).encode())
        io.interactive()


io = remote("00.cr.yp.toc.tf", 11337)
# io = process(["python", "did.py"])

[io.recvline() for _ in range(3)]
MOD = 127
oracle = Oracle()


def choose(X):
    """
    一意に定まるようなクエリを発行する
    """
    used = [False] * (MOD + 1)
    res = []
    for x in X:
        x2 = pow(x, 2, MOD)
        if used[x2] or used[x2 + 1]:
            continue
        used[x2] = True
        used[x2 + 1] = True
        res.append(x)
        if len(res) == 20:
            break
    return res


def roots(x):
    ans = []
    for a in range(MOD):
        if pow(a, 2, MOD) == x:
            ans.append(a)
    return ans


# 調査対象
X = set(range(MOD))

ans = set(range(MOD))
for _ in range(7):
    Y = choose(X)
    X -= set(Y)
    Z = oracle.send(Y)
    for z in Z:
        cand = roots(z) + roots(z - 1)
        assert sum([c in Y for c in cand]) == 1
        for c in cand:
            if c in Y:
                ans.remove(c)

assert len(ans) <= 20
oracle.answer(ans)
