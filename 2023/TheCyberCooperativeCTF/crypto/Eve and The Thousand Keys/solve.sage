from itertools import combinations, product
from Crypto.PublicKey import RSA
from math import gcd
from tqdm import tqdm
# from factordb.factordb import FactorDB

E, N = [], []
for i in range(1, 1001):
    # pub 形式の鍵を読み込む
    with open(f'public/key.{i}.pub') as f:
        pub = f.read()
        # 公開鍵情報を抜き出す
        pub = RSA.import_key(pub)
        E.append(pub.e)
        N.append(pub.n)
        print(pub)

assert set(E) == {65537}
assert len(set(N)) == 1000
assert set([n.bit_length() for n in N]) == {4095, 4096}

# 共通素数を持たないか → ない
# for m, n in tqdm(combinations(N, 2)):
#     assert gcd(m, n) == 1

# 既知の素因数を持たないか → 持たない
# for i, n in tqdm(enumerate(N)):
#     f = FactorDB(n)
#     f.connect()
#     factor = f.get_factor_list()
#     assert len(factor) == 1

# 小さな素因数を持たないか → 持たない
# for i, n in tqdm(enumerate(N)):
#     for x in range(2, 123456):
#         assert n % x != 0

# 単一の素数か → 違う
# for i, n in tqdm(enumerate(N)):
#     assert is_prime(n) == False

e = 65537

