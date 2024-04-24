from random import choice, sample
from operator import mul
from functools import reduce

# 333 bit の unsafe prime を見つける

P = []
for x in Primes():
    if x > 10**7:
        break
    P.append(x)

p = 1
S = [1]
while True:
    if (p + 1).bit_length() == 333 and is_prime(p + 1):
        print(factor(p))
        break
    print(p.bit_length())
    if 330 <= p.bit_length() < 333:
        for x in P:
            if (p * x).bit_length() == 333:
                p *= x
                break

    if p.bit_length() < 333:
        q = choice(P)
        p *= q
        S.append(q)
    else:
        T = sample(S, 5)
        p //= reduce(mul, T)
        for t in T:
            S.remove(t)
