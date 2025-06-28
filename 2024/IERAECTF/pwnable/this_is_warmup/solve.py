from z3 import *

a = BitVec("a", 64)
b = BitVec("b", 64)
s = Solver()

a_ = BV2Int(a, True)
b_ = BV2Int(b, True)
s.add(a_ * b_ >= a_)
s.add(a_ * b_ < b_)
s.add(0 < a_, a_ < 10**6)
s.add(a_ * b_ < 10**6)

print(s)

if s.check() == sat:
    m = s.model()
    print(m[a])
    print(m[b])
