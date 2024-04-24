# p^2 + q^2 == (p + iq) * (p - iq)
N = 180501716611818439995609435542731470075775193176428263372546170684067831289410
R = GaussianIntegers()
for d in divisors(R(N)):
    p, q = abs(int(d.real())), abs(int(d.imag()))
    if d.norm() == N and is_prime(p) and is_prime(q):
        break
print(p, q)
