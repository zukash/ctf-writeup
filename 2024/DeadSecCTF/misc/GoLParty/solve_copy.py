from pwn import *
import numpy as np


def update_grid(grid):
    n = grid.shape[0]
    new_grid = grid.copy()
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            # Calculate the number of live neighbors
            total = int(
                (
                    grid[i, (j - 1) % n]
                    + grid[i, (j + 1) % n]
                    + grid[(i - 1) % n, j]
                    + grid[(i + 1) % n, j]
                    + grid[(i - 1) % n, (j - 1) % n]
                    + grid[(i - 1) % n, (j + 1) % n]
                    + grid[(i + 1) % n, (j - 1) % n]
                    + grid[(i + 1) % n, (j + 1) % n]
                )
            )

            # Apply Conway's rules
            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    new_grid[i, j] = 0
            else:
                if total == 3:
                    new_grid[i, j] = 1
    return new_grid


# nc 34.132.190.59 30565
io = remote("34.132.190.59", "30565")
context.log_level = "DEBUG"

print(io.recvuntil(b"got!"))
print(io.recvline())
print(io.recvline())
print(io.recvline())
grid = io.recvuntil(b"[*]").replace(b"\xe2\x96\xa0", b"#").split()[:-1]
print(grid)
grid = [[int(chr(e) == "#") for e in row] for row in grid]
grid = np.array(grid)
print(grid)

m = io.recvregex(
    rb"Enter the number of live cells after (\d+) generations", capture=True
)
generation = int(m.group(1))

for _ in range(generation):
    grid = update_grid(grid)
    print(grid)

io.sendline(str(np.count_nonzero(grid)).encode())

io.interactive()
