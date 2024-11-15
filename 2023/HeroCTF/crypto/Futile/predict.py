import numpy
import random

SIZE = 32

def untemper(x):
    x = unBitshiftRightXor(x, 18)
    x = unBitshiftLeftXor(x, 15, 0xefc60000)
    x = unBitshiftLeftXor(x, 7, 0x9d2c5680)
    x = unBitshiftRightXor(x, 11)
    return x

def unBitshiftRightXor(x, shift):
    i = 1
    y = x
    while i * shift < 32:
        z = y >> shift
        y = x ^ z
        i += 1
    return y

def unBitshiftLeftXor(x, shift, mask):
    i = 1
    y = x
    while i * shift < 32:
        z = y << shift
        y = x ^ (z & mask)
        i += 1
    return y

SIZE = 32
# print(random.getrandbits(32))
# values1 = [numpy.random.randint(0, 1 << 32) for i in range(624)]
# values2 = [numpy.random.randint(0, 1 << 32) for i in range(624)]
values1 = [random.getrandbits(SIZE) for i in range(624)]
values2 = [random.getrandbits(SIZE) for i in range(624)]

mt_state = tuple([untemper(x) for x in values1] + [624])
random.setstate((3, mt_state, None))

predicted = [random.getrandbits(SIZE) for i in range(624)]
print(predicted == values2)
