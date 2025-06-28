from Crypto.Util.number import long_to_bytes

"""
computing discrete log for prime: 191
discrete log found: 25
computing discrete log for prime: 1621
discrete log found: 293
computing discrete log for prime: 61
discrete log found: 49
computing discrete log for prime: 2447
discrete log found: 2105
computing discrete log for prime: 991
discrete log found: 564
computing discrete log for prime: 1297
discrete log found: 50
computing discrete log for prime: 47
discrete log found: 13
computing discrete log for prime: 1049
discrete log found: 21
computing discrete log for prime: 347
discrete log found: 229
computing discrete log for prime: 283
discrete log found: 257
computing discrete log for prime: 2617
discrete log found: 307
computing discrete log for prime: 1429
discrete log found: 511
computing discrete log for prime: 167
discrete log found: 124
computing discrete log for prime: 307
discrete log found: 7
computing discrete log for prime: 431
discrete log found: 63
computing discrete log for prime: 683
discrete log found: 476
computing discrete log for prime: 1627
discrete log found: 1054
computing discrete log for prime: 17
discrete log found: 2
computing discrete log for prime: 827
discrete log found: 793
computing discrete log for prime: 97
discrete log found: 60
computing discrete log for prime: 523
discrete log found: 270
computing discrete log for prime: 151
discrete log found: 145
computing discrete log for prime: 37
discrete log found: 32
computing discrete log for prime: 2269
discrete log found: 796
computing discrete log for prime: 1733
discrete log found: 1041
computing discrete log for prime: 3
discrete log found: 1
computing discrete log for prime: 19
discrete log found: 9
computing discrete log for prime: 439
discrete log found: 60
"""

A = [
    25,
    293,
    49,
    2105,
    564,
    50,
    13,
    21,
    229,
    257,
    307,
    511,
    124,
    7,
    63,
    476,
    1054,
    2,
    793,
    60,
    270,
    145,
    32,
    796,
    1041,
    1,
    9,
    60,
]
M = [
    191,
    1621,
    61,
    2447,
    991,
    1297,
    47,
    1049,
    347,
    283,
    2617,
    1429,
    167,
    307,
    431,
    683,
    1627,
    17,
    827,
    97,
    523,
    151,
    37,
    2269,
    1733,
    3,
    19,
    439,
]

m = crt(A, M)
print(long_to_bytes(m))
