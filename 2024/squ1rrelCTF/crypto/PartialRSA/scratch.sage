from Crypto.Util.number import *
from tqdm import trange

n = 103805634552377307340975059685101156977551733461056876355507089800229924640064014138267791875318149345634740763575673979991819014964446415505372251293888861031929442007781059010889724977253624216086442025183181157463661838779892334251775663309103173737456991687046799675461756638965663330282714035731741912263
e = 3
flag = b"squ1rrel{dummy_dummy_dummy_dummy_dummy_du}"
print(len(flag))
# flag = b"squ1rrel{dummy}"
m = bytes_to_long(flag + flag)
ct = pow(m, e, n)

print(f"n = {n}")
print(f"e = {e}")
print(f"ct = {ct}")

# flag の長さで全探索
for i in trange(60):
    x = PolynomialRing(Zmod(n), "x").gen()
    f = (x * pow(2, 8 * i, n) + x) ** e - ct
    # f = x**e - ct
    roots = f.monic().small_roots(epsilon=0.015)
    if roots:
        print(long_to_bytes(int(roots[0])))
