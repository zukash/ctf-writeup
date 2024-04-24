flag = "a" * 0x54


def hash(flag, i):
    v4 = 0xCBF29CE484222325
    for j in range(4):
        v4 = (0x100000001B3 * (ord(flag[i + j]) ^ v4)) % (1 << 64)
    return v4


v9 = [hash(flag, i) for i in range(0, 0x54, 4)]

x = 123456789
y = 362436069
z = 521288629
w = -559038737

v10 = [0 for _ in range(0x54 // 4)]
for m in range(0x54 // 4):
    for n in range(0x54 // 4):
        v = (((x << 11) ^ x) >> 8) ^ (x << 11) ^ x
        x = y
        y = z
        z = w
        w ^= w >> 19
        w ^= v
        v10[m] = w % 1024 * v9[n]

print(v10)


v11 = [
    0xFFFFFF6F11B8034B,
    0x673420DAF2,
    0x45EB817F02C,
    0xFFFFFE3099503945,
    0x18F8DCE1227,
    0x26050EA6875,
    0x298599C4BF0,
    0xFFFFF8A356CE9E58,
    0xFFFFFED3C712CF36,
    0xFFFFFE96846D630F,
    0x58CB1CE3FF3,
    0xFFFFFCCF182C2A63,
    0xFFFFFE57FDF3F1DE,
    0xFFFFFA603F35F962,
    0xFFFFFF7884570B57,
    0x4897C4D9C1,
    0xFFFFFEB9355E5CB4,
    0xDCEDF7D094,
    0x3602E9CAC47,
    0xFFFFFEE3667219D6,
    0xFFFFFDC326C9B063,
]

for i in range(0x54 // 4):
    if v10[i] != v11[i]:
        print("Wrong")
        exit(0)
