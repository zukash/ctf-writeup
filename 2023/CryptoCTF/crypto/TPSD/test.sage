from itertools import count

# r = -r で置き換えて
# p**3 + q**3 == r**3 + 1
l = 3

p = next_prime(1 << l)
while True:
    print(p)
    for d in divisors(p ^ 3 + 1):
        x = var("x")
        f = 3 * x * x + 3 * d * x + d * d
        q, r = f.roots()
        q, r = q[0], r[0]
        if q.is_integer() and r.is_integer():
            print(q, r)
    p = next_prime(p)

"""
73 144 150
1033 1738 1852
"""
