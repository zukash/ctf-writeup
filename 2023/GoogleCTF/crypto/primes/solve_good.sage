from tqdm import tqdm

q = 0xD2F8711CB5502C512ACEA59BE181A8FCF12F183B540D9A6998BF66370F9538F7E39FC507545DAD9AA2E71D3313F0B4408695A0A2C03A790662A9BD01650533C584C90779B73604FB8157F0AB7C9A82E724700E5937D9FF5FCF1EE3BE1EDD7E07B4C0F035A58CC2B9DB8B79F176F595C1B0E90B7957309B96106A50A01B78171599B41C8744BCB1C0E6A24F60AE8946D37F4D4BD8CF286A336E1022996B3BA3918E4D808627D0315BFE291AEB884CBE98BB620DAA735B0467F3287D158231D
enc = 0x947062E712C031ADD0B60416D3B87D54B50C1EFBC8DBB87346F960B242AF3DF6DD47406FEC98053A967D28FE91B130FF0FE93689122931F0BA6E73A3E9E6C873B8E2344A459244D1295E99A241E59E1EEA796E9738E6B1EDEED3D91AE6747E8ECA634C030B90B02BAF8AE0088058F6994C7CAC232835AC72D8B23A96F10EF03D74F82C49D4513423DAC298698094B5C631B9C7C62850C498330E9D112BB9CAA574AEE6B0E5E66D5B234B23C755AC1719B4B68133E680A7BCF48B4CFD0924D

assert is_prime(q)


def to_bits(m):
    _bin = lambda b: [1 if b & (1 << n) else 0 for n in range(7)]
    return sum([_bin(b) for b in m], [])


def gen_primes(r, n):
    primes = Primes()[:n]
    bound = prod(primes[n - r :])
    return primes, next_prime(bound)


def prod_exp(p, q, b):
    return prod([p[i] ^ b[i] for i in range(len(p))]) % q


def encode(r, n, m):
    p, q = gen_primes(r, n)
    return p, q, prod_exp(p, q, to_bits(m))


# m = b"I have a sweet flag for you: CTF{YkDOLIStjpjP5Am1SXDt5d2r9es3b5KZP47v8rXF}"
target = b"YkDOLIStjpjP5Am1SXDt5d2r9es3b5KZP47v8rXF"
dummy = b"\x00" * len(target)
m = b"I have a sweet flag for you: CTF{" + dummy + b"}"
n = 7 * len(m)
p, q, x = encode(131, 7 * len(m), m)

print(to_bits(m))
P = Primes()[:n]
print(P)


def check(x):
    for p in P:
        if x % p == 0:
            x //= p
    return x == 1


flag = enc * pow(x, -1, q) % q

# 後半 SIZE 個を決めうち
SIZE = 22
for bit in tqdm(range(1 << SIZE)):
    t = flag
    S = [i for i in range(SIZE) if bit >> i & 1]
    # print([P[-s - 2] for s in S])
    for s in S:
        t *= pow(P[-8 - (s * 7)], -1, q)
        t %= q
    if check(t):
        print("found!")
        print(t)
