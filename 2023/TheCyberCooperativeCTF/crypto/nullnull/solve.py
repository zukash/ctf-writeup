from collections import defaultdict
import pickle

with open('data.pkl', 'rb') as f:
    S = pickle.load(f)

DD = [defaultdict(int) for _ in range(100)]
for s in S:
    for i, c in enumerate(s):
        DD[i][c] += 1

for D in DD:
    S = set(range(127)) - set(D.keys())
    assert len(S) == 1
    print(chr(S.pop()), end='')
