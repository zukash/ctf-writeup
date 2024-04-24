def lfsr(bit):
    for _ in range(1000):
        new = ((bit & 0x80) >> 7) ^ (bit & 0x01)
        bit = ((bit << 1) & 0xFF) ^ new
    return bit


enc = """
01001000 11010111 11010001 11001011 01011010 01000110 11011101 01001110 01001010 01110000 11010001 01110000 01011010 11010101 01001010 11001011 11000011
"""

print(bin(lfsr(ord("p"))))

D = {}
for c in range(256):
    D[lfsr(c)] = chr(c)

for c in enc.split():
    print(D[int(c, 2)], end="")


# io.interactive()
