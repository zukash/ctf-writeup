from itertools import permutations
from tqdm import tqdm
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes


def rearrange(S, order):
    pem = ""
    for i in range(0, len(S), 10):
        Q = [chr(int(c, 16)) for c in S[i : i + 10]]
        pem += "".join(Q[j] for j in order if j < len(Q))
    return pem


private = open("private").read().strip().split()
public = open("public").read().strip().split()

# 必要条件で絞る
# private = private[:20]
# for order in tqdm(permutations(range(10))):
#     S = rearrange(order)
#     # print(S.split("\n")[0])

#     if S.split("\n")[0] == "-----BEGIN PRIVATE KEY-----"[:20]:
#         print(order)

order = (8, 6, 9, 5, 7, 3, 1, 4, 0, 2)
private_key = RSA.import_key(rearrange(private, order))

e, n, d = private_key.e, private_key.n, private_key.d
enc = open("flag.txt.enc", "rb").read()
flag = pow(bytes_to_long(enc), d, n)
print(long_to_bytes(flag))
