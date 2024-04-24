import galois
import numpy as np

MOD = 7514777789

points = []

for line in open("encoded.txt", "r").read().strip().split("\n"):
    x, y = line.split(" ")
    points.append((int(x), int(y)))

# GF = galois.GF(MOD)

# matrix = []
# solution = []
# for point in points:
#     x, y = point
#     solution.append(GF(y % MOD))

#     row = []
#     for i in range(len(points)):
#         row.append(GF((x**i) % MOD))

#     matrix.append(GF(row))
points = points[:1000]

print(len(points))
print(*[x for x, y in points])
print(*[y for x, y in points])
# open('output.bmp', 'wb').write(bytearray(np.linalg.solve(GF(matrix), GF(solution)).tolist()[:-1]))
