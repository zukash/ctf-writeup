sage.structure.element.is_Matrix = lambda z: isinstance(z, sage.structure.element.Matrix)
# See README.md for this package
from vector_bundle import *
from string import printable
from tqdm import tqdm


p = 66036476783091383193200018291948785097
F = GF(p)
K.<x> = FunctionField(F)
print(K)
print(x)
print(x.zeros()[0])
print(x.zeros()[0].divisor())

L = VectorBundle(K, -x.zeros()[0].divisor()) # L = O(-1)

print(L)

V = L.tensor_power(1)
print(V)
V = V.direct_sum(L.tensor_power(2))
print(V)
print(V.tensor_product(L.tensor_power(3)).h0())


# for b in tqdm(password[1:]):
#     V = V.direct_sum(L.tensor_power(b))

# L = L.dual() # L = O(1)
# out = [
#     len(V.tensor_product(L.tensor_power(m)).h0())
#     for m in tqdm(printable.encode())
# ]