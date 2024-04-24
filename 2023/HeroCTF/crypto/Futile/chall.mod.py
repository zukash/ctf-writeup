#!/usr/bin/env python
from pylfsr import LFSR
from functools import reduce
import os
import numpy


flag = os.environ.get('FLAG','Hero{fake_flag}').encode()

def binl2int(l: list) -> int:
    return reduce(lambda x,y: 2*x+y, l)

def lfsr() -> LFSR:
    # https://github.com/Nikeshbajaj/Linear_Feedback_Shift_Register
    return LFSR(fpoly=[8,6,5,4], initstate='random')

def get_uint8() -> int:
    # 単純にinitstateを取り出しているだけ？？
    bit = lfsr().runKCycle(8)
    print(bit)
    return binl2int(bit)

def mask(flag: bytes) -> str:
    return bytearray(f ^ get_uint8() for f in flag).hex()

numpy.random.seed(1234)

while True:
    try:
        input('Hero{' + mask(flag[5:-1]) + '}\n')
    except Exception as e:
        pass
