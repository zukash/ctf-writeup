from unicodedata import numeric
from itertools import product
import sys
from fractions import Fraction
from tqdm import tqdm


text = "*" * 12345678 + "FAKECTF{THIS_IS_FAKE}" + "*" * 12345678


# I made a simple calculator :)
def calc(s):
    if (loc := s.find("+")) != -1:
        return calc(s[:loc]) + calc(s[loc + 1 :])
    if (loc := s.find("*")) != -1:
        return calc(s[:loc]) * calc(s[loc + 1 :])
    x = 0
    for c in s:
        x = 10 * x + numeric(c)
    return x


def check(s):
    if not all(c.isnumeric() or c in "+*" for c in s):
        return False
    if len(s) >= 6:  # I don't like long expressions!
        return False
    return True


chars = "".join(map(chr, range(sys.maxunicode + 1)))
# digits = "".join(filter(str.isdigit, chars))
numerics = "".join(filter(str.isnumeric, chars))
print(len(numerics))
nums = list(map(numeric, numerics))
print(numerics)
print(sorted(set(nums)))
print(numerics[nums.index(-0.5)])
print(numerics[nums.index(12.0)])
print(numerics[nums.index(0.1111111111111111)])
fractions = [Fraction(num).limit_denominator() for num in sorted(set(nums))]
print(fractions)
# ⅑*⅑*億

D = {numeric(n): n for n in numerics}
print(D)
S = set()
alphabet = list(D.values()) + list("+*")
for k in range(1, 5):
    for s in tqdm(product(alphabet, repeat=k)):
        s = "".join(s)
        assert check(s)
        val = int(calc(s))
        if 1234563 <= val <= 1234570:
            print(val, s)
        # S.add(val)

# print(sorted(S))
