import random

# *******************************************
# getrandbits の挙動
# *******************************************


random.seed(1337)
X = [random.getrandbits(32) >> 31 for _ in range(100)]
random.seed(1337)
Y = [random.getrandbits(1) for _ in range(100)]

assert X == Y


# *******************************************
# Untwister の挙動
# *******************************************
rands = list(open("output.txt").read().strip())

from symbolic_mersenne_cracker import Untwister
import random
from math import ceil

r1 = random.Random()
ut = Untwister()
for r in rands:
    # Just send stuff like "?11????0011?0110??01110????01???"
    # Where ? represents unknown bits
    print(r + "?" * 31)
    ut.submit(r + "?" * 31)

r2 = ut.get_random()
print(r2.getstate())
# for _ in range(624):
#     assert r1.getrandbits(32) == r2.getrandbits(32)

# print("Test passed!")
