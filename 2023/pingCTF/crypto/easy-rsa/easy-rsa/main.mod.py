from Crypto.Util.number import getPrime
from Crypto.Util.number import bytes_to_long

p = getPrime(8)
q = getPrime(8)
n = p * q
e = 65537
d = pow(e, -1, (p-1)*(q-1))
flag = open("flag.txt","rb").read()

print(f"q & p = {q & p}")
print(f"q & (p << 1) = {q & (p << 1)}")
print(f"n = {n}")
print(f"ct = {pow(bytes_to_long(flag), e, n)}")

h0 = q & p
h1 = q & (p << 1)

print(f'{p = }')
print(f'{q = }')
print(f"q & p = {bin(q & p)}")
print(f"q & (p << 1) = {bin(q & (p << 1))}")
print(f'{bin(p ) = }')
print(f'{bin(q ) = }')
print(f'{bin(h0) = }')
print(f'{bin(h1) = }')
r = h0 | h1
print(f'{bin(r ) = }')
s = h0 | (h1 >> 1)
print(f'{bin(s ) = }')
