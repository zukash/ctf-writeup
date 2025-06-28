from Crypto.Util.number import long_to_bytes
from params import n, e, c, phi

# "phi" = (p + 1) * (q + 1) = p * q + p + q + 1 = n + p + q + 1
# phi = (p - 1) * (q - 1) = p * q - p - q + 1 = n - (p + q) + 1
p_q = phi - n - 1
phi = n - p_q + 1

d = pow(e, -1, phi)
m = pow(c, d, n)
print(long_to_bytes(m))
