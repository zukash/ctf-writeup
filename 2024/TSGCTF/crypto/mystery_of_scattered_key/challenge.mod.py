from Crypto.Util.number import getStrongPrime
from random import shuffle

flag = b"FAKE{THIS_IS_FAKE_FLAG}"


p = getStrongPrime(1024)
q = getStrongPrime(1024)

N = p * q
e = 0x10001
m = int.from_bytes(flag, "big")
c = pow(m, e, N)


# "Aaaaargh!" -- A sharp, piercing scream shattered the silence.

p_bytes = p.to_bytes(128, "big")
q_bytes = q.to_bytes(128, "big")

fraction_size = 2
p_splitted = [
    int.from_bytes(p_bytes[i : i + fraction_size], "big")
    for i in range(0, len(p_bytes), fraction_size)
]
q_splitted = [
    int.from_bytes(q_bytes[i : i + fraction_size], "big")
    for i in range(0, len(q_bytes), fraction_size)
]

shuffle(p_splitted)
shuffle(q_splitted)

D = {}
for ip, p in enumerate(p_splitted):
    for iq, q in enumerate(q_splitted):
        assert p * q % (256**2) not in D
        D[p * q % (256**2)] = (ip, iq)

# print((p_splitted[-1] * q_splitted[-1]) % (256**2))
# print((p * q) % (256**2))
# print(N % (256**2))
# assert (p_splitted[-1] * q_splitted[-1]) % (256**4) == N % (256**4)
print(D[N % (256**2)])

# print(p_splitted[-1] * q_splitted[-1])
# print(p_splitted[0] * q_splitted[0])
# print(N)


# print(f"N = {N}")
# print(f"c = {c}")
# print(f"p_splitted = {p_splitted}")
# print(f"q_splitted = {q_splitted}")
