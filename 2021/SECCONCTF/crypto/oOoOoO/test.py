from Crypto.Util.number import *
from ctftools.crypto.lll import subset_sum_problem

m = 4250752392863654689979306659669983891404173288681822936074995285481021474298300375938288879206302630759317724607850013961329108618771089923530772971082383851388802018414762444056197873524176249
s = 3118444024780191287539688465744528158102422854082886971475956280625703108074576561562608200107931365458999914609314125290873947619612132640729857236854784313842385569830514221942316942179725961
message = b"oOooOOooOoOOoOooooOOOooOOoooooooOOOoooooOoooOooooooOoOoOoOoOoOOOooOOOooOOoOOoOOooooooooooooooOooOOoooooOooOOOOooOoooOOooooOoOooO"
n = len(message)

assert bytes_to_long(message) % m == s

P = [pow(256, n - i - 1, m) for i in range(n)]
S = [c * P[i] % m for i, c in enumerate(message)]
sumS = sum(S)
assert sum(S) % m == s

P = [pow(256, n - i - 1, m) for i in range(n)]
X = [ord("O") * P[i] % m for i, c in enumerate(message)]
S = [(ord("o") - ord("O")) * P[i] % m for i, c in enumerate(message) if c == ord("o")]
assert (sum(S) + sum(X)) % m == s
assert sum(S) % m == (s - sum(X)) % m

t = (s - sum(X)) % m
k = (sum(S) - t) // m
S = [(ord("o") - ord("O")) * P[i] % m for i, c in enumerate(message)]
I = [int(c == ord("o")) for i, c in enumerate(message)]
assert sum([s * i for s, i in zip(S, I)]) % m == t
assert sum([s * i for s, i in zip(S, I)]) == t + k * m

ans = subset_sum_problem(S, t + k * m, verbose=False)
ans = "".join(["Oo"[x] for x in ans])
assert ans == message.decode()
