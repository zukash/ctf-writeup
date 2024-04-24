from itertools import product

flag = "a" * 0x54


def hash(flag, i):
    v4 = 0xCBF29CE484222325
    for j in range(4):
        v4 = (0x100000001B3 * (ord(flag[i + j]) ^^ v4)) % (1 << 64)
    return v4



# v9 = [hash(flag, i) for i in range(0, 0x54, 4)]
v9 = [var('v9_' + str(i)) for i in range(0x54 // 4)]

# v11 = [
#     0xFFFFFF6F11B8034B,
#     0x673420DAF2,
#     0x45EB817F02C,
#     0xFFFFFE3099503945,
#     0x18F8DCE1227,
#     0x26050EA6875,
#     0x298599C4BF0,
#     0xFFFFF8A356CE9E58,
#     0xFFFFFED3C712CF36,
#     0xFFFFFE96846D630F,
#     0x58CB1CE3FF3,
#     0xFFFFFCCF182C2A63,
#     0xFFFFFE57FDF3F1DE,
#     0xFFFFFA603F35F962,
#     0xFFFFFF7884570B57,
#     0x4897C4D9C1,
#     0xFFFFFEB9355E5CB4,
#     0xDCEDF7D094,
#     0x3602E9CAC47,
#     0xFFFFFEE3667219D6,
#     0xFFFFFDC326C9B063,
# ]

v11 = [216589915878108112827126, 194528196343631108021949, 179478888862947034287753, 178242443412656089262643, 157682121924960946273671, 180008794055928867869943, 194051281669947457797978, 165948642935477550155835, 153566524926135372118662, 185166537934285381403259, 237291545417265078104682, 185943732217325403990471, 200993039698009477724667, 189034845843052766553246, 175946187576401477073153, 134542928498087546518041, 237044256327206889099660, 166655183192786661598755, 206239101108529630188348, 175504599915583282421328, 242837886437141602931604]

x = 123456789
y = 362436069
z = 521288629
w = -559038737

equations = []
v10 = [0 for _ in range(0x54 // 4)]
for m in range(0x54 // 4):
    for n in range(0x54 // 4):
        v = x ^^ (x << 0xB)
        x = y
        y = z
        z = w
        w = w ^^ (w >> 0x13) ^^ v ^^ (v >> 8)
        v10[m] += w % 1024 * v9[n]
    equations.append(v10[m] == v11[m])

print(equations)
print(v10)
ans = solve(equations, *v9)



D = {}
alphabet = list("!_acdefghilmnoprstuwy")
for S in product(alphabet, repeat=4):
    S = "".join(S)
    if hash(S, 0) in D:
        print("Collision")
    D[hash(S, 0)] = S

for x in ans[0]:
    print(D[x.rhs()])