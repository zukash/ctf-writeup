from Crypto.Util.number import *
from ctftools.crypto.lll import subset_sum_problem
from pwn import *
from tqdm import trange

io = process(["python3", "problem.py"])

m = int(io.recvline().split(b"=")[1])
s = int(io.recvline().split(b"=")[1])
message = io.recvline().split(b"=")[1].strip()
n = len(message)

P = [256 ** (n - i - 1) for i in range(n)]
X = [ord("O") * P[i] % m for i, c in enumerate(message)]
S = [(ord("o") - ord("O")) * P[i] % m for i, c in enumerate(message)]
t = (s - sum(X)) % m

for i in trange(128):
    ans = subset_sum_problem(S, t + i * m, verbose=False)
    if ans:
        ans = "".join(["Oo"[x] for x in ans])
        io.sendline(ans)
        io.interactive()
