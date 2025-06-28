from itertools import product
from pwn import *

context.arch = "amd64"

P = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113,
    127,
    131,
    137,
    139,
    149,
    151,
    157,
    163,
    167,
    173,
    179,
    181,
    191,
    193,
    197,
    199,
    211,
    223,
    227,
    229,
    233,
    239,
    241,
    251,
]

for k in range(3, 4):
    for ope in product(P, repeat=k):
        shellcode = disasm(bytes(ope))
        if "(bad)" in shellcode:
            continue
        if ".byte" in shellcode:
            continue
        if "1:" in shellcode:
            continue
        if "2:" in shellcode:
            continue
        print(shellcode)


"""
   0:   43                      rex.XB
   0:   47                      rex.RXB
   0:   49                      rex.WB
   0:   4f                      rex.WRXB
   0:   53                      push   rbx
   0:   59                      pop    rcx
   0:   65                      gs
   0:   67                      addr32
   0:   6d                      ins    DWORD PTR es:[rdi], dx
   0:   95                      xchg   ebp, eax
   0:   97                      xchg   edi, eax
   0:   9d                      popf
   0:   a7                      cmps   DWORD PTR ds:[rsi], DWORD PTR es:[rdi]
   0:   ad                      lods   eax, DWORD PTR ds:[rsi]
   0:   ef                      out    dx, eax
   0:   f1                      int1
   0:   fb                      sti
"""