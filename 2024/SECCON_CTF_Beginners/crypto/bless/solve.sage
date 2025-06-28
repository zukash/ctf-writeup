import json
from tqdm import trange

q = 0x1a0111ea397fe69a4b1ba7b6434bacd764774b84f38512bf6730d2a0f6b0f6241eabfffeb153ffffb9feffffffffaaab
r = 0x73eda753299d7d483339d80809a1d80553bda402fffe5bfeffffffff00000001

F = GF(q, x, x)
F2.<i> = GF(q^2, "i", x^2 + 1)
F12.<w> = GF(q**12, "w", x**12 - 2*x**6 + 2)

i12 = w**6 - 1
z = w^-1

E1 = EllipticCurve(F, [0, 4])
E2 = EllipticCurve(F2, [0, 4*(1+i)])
E12 = EllipticCurve(F12, [0, 4])


def F2_to_F12(coeffs):
    assert len(coeffs) == 2
    c = coeffs[0]
    d = coeffs[1]
    x = c + d*i12

    return x


def sextic_twist(Px, Py):
    x = F2_to_F12(Px)
    y = F2_to_F12(Py)

    return E12(z^2*x, z^3*y)

# G1 = E1(0x17F1D3A73197D7942695638C4FA9AC0FC3688C4F9774B905A14E3A3F171BAC586C55E83FF97A1AEFFB3AF00ADB22C6BB, 0x08B3F481E3AAA0F1A09E30ED741D8AE4FCF5E095D5D00AF600DB18CB2C04B3EDD03CC744A2888AE40CAA232946C5E7E1)
G1 = E12(F(4), F(0x0a989badd40d6212b33cffc3f3763e9bc760f988c9926b26da9dd85e928483446346b8ed00e1de5d5ea93e354abe706c)) * 0x396c8c005555e1568c00aaab0000aaab
G2 = E12(z^2*2, z^3*(0x013a59858b6809fca4d9a3b6539246a70051a3c88899964a42bc9a69cf9acdd9dd387cfa9086b894185b9a46a402be73 + 0x02d27e0ec3356299a346a09ad7dc4ef68a483c3aed53f9139d2f929a3eecebf72082e5e58c6da24ee32e03040c406d4f*i12)) * 0x5d543a95414e7f1091d50792876a202cd91de4547085abaa68a205b2e5a7ddfa628f1cb4d9e82ef21537e293a6691ae1616ec6e786f0c70cf1c38e31c7238e5

with open("output.org.json") as f:
    out_list = json.load(f)

flag = ""
for out in out_list:
    PAx = out["P"]["x"]
    PAy = out["P"]["y"]
    PA = E12(PAx, PAy)
    PBx = list(map(int, out["Q"]["x"]))
    PBy = list(map(int, out["Q"]["y"]))
    PB = sextic_twist(PBx, PBy)
    use_F2 = len(out["R"]["x"]) == 2
    assert use_F2
    for c in trange(1, 256):
        e_aGbG = PA.tate_pairing(c * PB, r, 12)
        if use_F2:
            PCx = list(map(int, out["R"]["x"]))
            PCy = list(map(int, out["R"]["y"]))
            PC = sextic_twist(PCx, PCy)
            res = G1.tate_pairing(PC, r, 12)
        else:
            PCx = int(out["R"]["x"][0], 16)
            PCy = int(out["R"]["y"][0], 16)
            PC = E12(PCx, PCy)
            res = PC.tate_pairing(G2, r, 12)
        # print(res)
        if res == e_aGbG:
            print(chr(c))
            flag += chr(c)
            break
    # flag_bits += "1" if res == e_aGbG else "0"

    # if len(flag_bits) % 8 == 0:
    #     flag = int.to_bytes(int(flag_bits, 2), len(flag_bits) // 8, "big")
    #     print(flag)

print(flag)