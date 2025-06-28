from pwn import *
import numpy as np

DIR = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]


def update_grid(grid):
    m, n = grid.shape
    new_grid = grid[:]
    for i in range(m):
        for j in range(n):
            total = 0
            for di, dj in DIR:
                ni, nj = i + di, j + dj
                if not (0 <= ni < m and 0 <= nj < n):
                    continue
                total += grid[ni, nj]

            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    new_grid[i, j] = 0
            else:
                if total == 3:
                    new_grid[i, j] = 1
    return new_grid


io = remote("34.69.226.63", "32249")
context.log_level = "DEBUG"

io.recvuntil(b"Game On :D")
grid = io.recvuntil(b"[*]").replace(b"\xe2\x96\xa0", b"#").split()[1:-1]
print(grid)
grid = [[int(chr(e) == "#") for e in row] for row in grid]
print(grid)
grid = np.array(grid)
print(grid.shape)

m = io.recvregex(
    rb"Enter the number of live cells after (\d+) generations", capture=True
)
generation = int(m.group(1))
print(generation)

for _ in range(generation):
    grid = update_grid(grid)

    # for row in grid:
    #     print("".join(map(str, row)).replace("0", ".").replace("1", "#"))
    # print("************************")


m, n = grid.shape
io.sendlineafter(b":", str(np.count_nonzero(grid)).encode())

io.interactive()
