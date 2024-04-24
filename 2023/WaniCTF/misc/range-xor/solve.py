from  collections import defaultdict
A = [*map(int, input().split())]
n = len(A)
MOD = 10**9+7

def f(x):
    return min(x, 1000 - x)

dp = defaultdict(int)
dp[0] = 1

for a in A:
    ndp = defaultdict(int)
    for k, v in dp.items():
        if f(a) != a:
            ndp[k ^ f(a)] += v
        ndp[k ^ a] += v
    dp = ndp
    
ans = sorted(dp.items())[0][1]
print(ans % MOD)


"""
532 746 606 601 293 825 912 826 789 190
"""