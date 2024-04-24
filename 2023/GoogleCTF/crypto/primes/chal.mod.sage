# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tqdm import tqdm


def to_bits(m):
    _bin = lambda b: [1 if b & (1 << n) else 0 for n in range(7)]
    return sum([_bin(b) for b in m], [])


def gen_primes(r, n):
    primes = Primes()[:n]
    bound = prod(primes[n - r :])
    print(len(primes), primes)
    print(bound)
    return primes, next_prime(bound)


def prod_exp(p, q, b):
    print(len(p), len(b))
    print([p[i] ^ b[i] for i in range(len(p))])
    return prod([p[i] ^ b[i] for i in range(len(p))])
    # return prod([p[i] ^ b[i] for i in range(len(p))]) % q


def encode(r, n, m):
    p, q = gen_primes(r, n)
    return p, q, prod_exp(p, q, to_bits(m))


m = b"I have a sweet flag for you: CTF{YkDOLIStjpjP5Am1SXDt5d2r9es3b5KZP47v8rXF}"
p0, q0, x0 = encode(131, 7 * len(m), m)


target = b"YkDOLIStjpjP5Am1SXDt5d2r9es3b5KZP47v8rXF"
dummy = b"\x00" * len(target)
m = b"I have a sweet flag for you: CTF{" + dummy + b"}"
p1, q1, x1 = encode(131, 7 * len(m), m)

n = 7 * len(m)
P = Primes()[:n]


def check(x):
    for p in P:
        if x % p == 0:
            x //= p
    return x == 1


assert x0 % x1 == 0
ans = x0 // x1
print(factor(ans))
assert check(ans)
assert q0 == q1

q = q0
t = (
    3391
    * 3407
    * 3433
    * 3449
    * 3457
    * 3469
    * 3491
    * 3499
    * 3527
    * 3539
    * 3541
    * 3547
    * 3581
    * 3583
    * 3607
    * 3617
    * 3623
    * 3659
)

assert ans % t == 0
ans //= t
# ans *= pow(t, -1, q)
# ans %= q
print(ans)
assert ans < q
# # 後半 SIZE 個を決めうち
# SIZE = 20
# for bit in tqdm(range(1 << SIZE)):
#     t = ans
#     S = [i for i in range(SIZE) if bit >> i & 1]
#     # print([P[-s - 2] for s in S])
#     for s in S:
#         t *= pow(P[-s - 2], -1, q)
#         t %= q
#     if check(t):
#         print("found!")
#         print(t)
