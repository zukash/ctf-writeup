from pwn import *
from itertools import product
from collections import defaultdict
import random

io = process(["python3", "minesweeper.py"])

# グリッド情報
dims = [20, 20, 5, 5]
size = len(dims)

# 既に開いたマスとその周囲地雷数
borders = {}
revealed = set()
flags = set()


def neighbors(cell):
    for offset in product([-1, 0, 1], repeat=size):
        if any(offset):
            nbr = tuple(cell[i] + offset[i] for i in range(size))
            if all(0 <= nbr[i] < dims[i] for i in range(size)):
                yield nbr


def submit(point):
    if point in revealed or point in flags:
        return True
    io.sendlineafter(b":", " ".join(map(str, point)).encode())
    res = io.recvuntil(b"Enter")
    boom = False
    for row in res.split(b"\n"):
        row = row.strip()
        if b"BOOM!" in row:
            print("BOOM! at", point)
            boom = True
        if b"has" in row:
            row = row.removesuffix(b"bordering mine(s).")
            p_str, bc = row.split(b" has ")
            p = eval(p_str.decode())
            borders[p] = int(bc)
            revealed.add(p)
    return not boom


def infer_safe_and_mines():
    safe = set()
    mines = set()
    for cell, count in borders.items():
        unrevealed = []
        flagged = 0
        for nbr in neighbors(cell):
            if nbr in flags:
                flagged += 1
            elif nbr not in revealed:
                unrevealed.append(nbr)

        if not unrevealed:
            continue

        if count == flagged:
            safe.update(unrevealed)
        elif count - flagged == len(unrevealed):
            mines.update(unrevealed)
    return safe - revealed, mines - flags


# 初手：安全確保のために中心をクリック
submit(tuple(d // 2 for d in dims))

# 自動解法ループ
while True:
    safe, mines = infer_safe_and_mines()

    if mines:
        for m in mines:
            flags.add(m)
            print(f"Flagged: {m}")

    if safe:
        for s in safe:
            if not submit(s):
                exit("💥 Hit a mine!")
    else:
        # 推測フェーズ（単純ランダム）
        candidates = [
            p
            for p in product(*(range(d) for d in dims))
            if p not in revealed and p not in flags
        ]
        if not candidates:
            break
        guess = random.choice(candidates)
        print(f"Guessing: {guess}")
        if not submit(guess):
            exit("💥 Hit a mine!")

    if len(revealed) + len(flags) == len(list(product(*(range(d) for d in dims)))):
        print("🎉 Solved! All cells accounted for.")
        break

io.interactive()
