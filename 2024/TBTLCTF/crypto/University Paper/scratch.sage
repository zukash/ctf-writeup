p = next_prime(1 << 512)

m = 1 << 512
a = m**2 % p
x = PolynomialRing(GF(p), "x").gen()
f = x**2 - a


# p = next_prime(1 << 512)
# q = next_prime(p)
p = 11
q = 13
n = p * q
m = 123
a = m**2 % n
x = PolynomialRing(Zmod(n), "x").gen()
f = x**2 - a

print(f.roots(multiplicities=False))
