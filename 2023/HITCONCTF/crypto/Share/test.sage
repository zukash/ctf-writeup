import tqdm

# p = 115792089237316195423570985008687907853269984665640564039457584007913129640233
# p = next_prime(1 << 30)
# p = next_prime(200)
# for n in tqdm.trange(2, 200):
#     M = []
#     for i in range(n):
#         M.append([pow(i + 1, j, p) for j in range(n)])
#     Z = Zmod(p)
#     M = matrix(Z, M)
#     M = M[0:-1, 1:]
#     print(n)
#     assert n - 1 == M.rank()


n = 14
for p in Primes():
    if p < 14:
        continue
    M = []
    for i in range(n):
        M.append([pow(i + 1, j, p) for j in range(n)])
    Z = Zmod(p)
    M = matrix(Z, M)
    M = M[0:-1, 1:]
    print(p)
    assert n - 1 == M.rank()
