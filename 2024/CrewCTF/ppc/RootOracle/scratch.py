from collections import Counter

# b**2 - 4 * a * c

C = Counter()
for a in range(100):
    for b in range(100):
        for c in range(100):
            C[b**2 - 4 * a * c] += 1

print(C)
