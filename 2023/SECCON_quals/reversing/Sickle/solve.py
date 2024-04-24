# reversed source code
from Crypto.Util.number import *

B = [
    8215359690687096682,
    1862662588367509514,
    8350772864914849965,
    11616510986494699232,
    3711648467207374797,
    9722127090168848805,
    16780197523811627561,
    18138828537077112905,
]
e = 65537
p = 18446744073709551557
d = pow(e, -1, p - 1)
init = 1244422970072434993
flag = b""
for b in B:
    ai = pow(b, d, p)
    a = ai ^ init
    init = b
    flag += long_to_bytes(a)[::-1]
print(flag)


def main():
    flag = "a" * 64  # from input

    if len(flag) != 64:
        return

    ok = True
    for i in range(64):
        ok &= flag[i] <= 127
    if not ok:
        return

    a = []
    for i in range(8):
        a.append(int.from_bytes(flag[i * 8 : (i + 1) * 8], "little"))

    b = []
    init = 1244422970072434993
    for i in range(8):
        b.append(pow(a[i] ^ init, 65537, 18446744073709551557))
        init = b[-1]

    return b == [
        8215359690687096682,
        1862662588367509514,
        8350772864914849965,
        11616510986494699232,
        3711648467207374797,
        9722127090168848805,
        16780197523811627561,
        18138828537077112905,
    ]


if main():
    print("やったー")
