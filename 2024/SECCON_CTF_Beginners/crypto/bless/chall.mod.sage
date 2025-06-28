import json
import os

FLAG = os.getenv("FLAG", "ctf4b{*** REDACTED ***}").encode()

# https://neuromancer.sk/std/bls/BLS12-381
p = 0x1A0111EA397FE69A4B1BA7B6434BACD764774B84F38512BF6730D2A0F6B0F6241EABFFFEB153FFFFB9FEFFFFFFFFAAAB
q = 0x73EDA753299D7D483339D80809A1D80553BDA402FFFE5BFEFFFFFFFF00000001
F1 = GF(p)
E1 = EllipticCurve(F1, (0, 4))

F2 = GF(p ^ 2, "x", modulus=x ^ 2 + 1)
E2 = EllipticCurve(F2, (0, 4 * (1 + F2.gen())))

G1 = (
    E1(
        F1(4),
        F1(
            0x0A989BADD40D6212B33CFFC3F3763E9BC760F988C9926B26DA9DD85E928483446346B8ED00E1DE5D5EA93E354ABE706C
        ),
    )
    * 0x396C8C005555E1568C00AAAB0000AAAB
)
# G2 = (
#     E2(
#         F2(2),
#         F2(
#             0x013A59858B6809FCA4D9A3B6539246A70051A3C88899964A42BC9A69CF9ACDD9DD387CFA9086B894185B9A46A402BE73
#             + 0x02D27E0EC3356299A346A09AD7DC4EF68A483C3AED53F9139D2F929A3EECEBF72082E5E58C6DA24EE32E03040C406D4F
#             * F2.gen()
#         ),
#     )
#     * 0x5D543A95414E7F1091D50792876A202CD91DE4547085ABAA68A205B2E5A7DDFA628F1CB4D9E82EF21537E293A6691AE1616EC6E786F0C70CF1C38E31C7238E5
# )
G2 = E2.random_point()


def to_dict(P):
    if P.base_ring() == F1:
        return {"x": int(P[0]), "y": int(P[1])}
    else:
        Px, Py = P[0].polynomial(), P[1].polynomial()
        return {"x": [int(Px[0]), int(Px[1])], "y": [int(Py[0]), int(Py[1])]}


challenges = []
for c in FLAG:
    s, t = randrange(q), randrange(q)
    challenges.append(
        {"P": to_dict(s * G1), "Q": to_dict(t * G2), "R": to_dict(c * s * t * G2)}
    )

with open("output.json", "w") as f:
    json.dump(challenges, f)
