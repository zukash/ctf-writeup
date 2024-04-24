from string import printable

gen = 337
flag = [
    151,
    825,
    151,
    629,
    1021,
    1131,
    488,
    48,
    880,
    1059,
    911,
    457,
    48,
    261,
    911,
    292,
    385,
    292,
    206,
    103,
    911,
    739,
    48,
    684,
    598,
    1059,
    911,
    770,
    457,
    911,
    488,
    244,
    206,
    292,
    653,
]

D = {gen * ord(c) % 1152: c for c in printable}
print(D)

flag = "".join(D[f] for f in flag)
print(flag)
