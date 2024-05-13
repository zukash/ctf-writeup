X = [
    80365906,
    1769232938,
    1128934032,
    919644615,
    268622536,
    76757739,
    1906480421,
    1839781169,
    1764071040,
    561586492,
    1569349783,
    1791633442,
    1419111682,
    626666709,
    380985946,
    780831418,
    762273460,
    1434245458,
    750052501,
    34417081,
    244000852,
    1179042137,
    1198822017,
    1411554630,
    1813829152,
    133697279,
    78464676,
    854310990,
    1336677923,
    1611538180,
    617426944,
]


def no():
    print("Skulking around Knockturn Alley? Dodgy place...")
    print(c)
    exit()


def sub_11CA(a1, a2, a3):
    result = M[31 * a1 + a2] == "1"
    if (M[31 * a1 + a2] == "1") != (((X[a3 // 31] >> (31 - a3 % 31 - 1)) & 1) != 0):
        no()
    return result


print("Now don't forget to speak very, very clearly...")
# M = []
# for i in range(31):
#     bits = input()
#     if len(bits) != 31:
#         no()
#     M.extend(bits)
#     for j in range(31):
#         if M[31 * i + j] != "0" and M[31 * i + j] != "1":
#             no()

i = 0
j = 0
c = 0
up = 1
Q = []
while i < 31 and j < 31:
    Q.append((i, j, c))
    # sub_11CA(i, j, c)
    c += 1

    if up == 1:
        ni = i - 1
        nj = j + 1
    else:
        ni = i + 1
        nj = j - 1

    if ni < 0 or ni == 31 or nj < 0 or nj == 31:
        if up == 1:
            i += j == 30
            j += j < 30
        else:
            j += i == 30
            i += i < 30
        up = 1 - up
    else:
        i = ni
        j = nj

# print(Q)
print("Welcome to Diagon Alley!")

ans = [[0] * 31 for _ in range(31)]
for i, j, c in Q:
    expected = ((X[c // 31] >> (31 - c % 31 - 1)) & 1) != 0
    ans[i][j] = int(expected)

for row in ans:
    print("".join(["⬛️" if x else "⬜️" for x in row]))
