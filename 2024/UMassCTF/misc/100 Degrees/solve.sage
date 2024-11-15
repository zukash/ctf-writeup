from collections import defaultdict


p = 137

DAY = defaultdict(int)

DAY[0] = 81
DAY[1] = 67
DAY[2] = 110
DAY[3] = 116
DAY[4] = 49
DAY[5] = 111
DAY[6] = 74
DAY[7] = 53
DAY[8] = 93
DAY[9] = 83
DAY[10] = 55
DAY[11] = 122
DAY[12] = 67
DAY[13] = 47
DAY[14] = 85
DAY[15] = 91
DAY[16] = 88
DAY[17] = 84
DAY[18] = 63
DAY[19] = 96
DAY[20] = 59
DAY[21] = 87
DAY[22] = 46
DAY[23] = 99
DAY[24] = 93
DAY[25] = 126
DAY[26] = 62
DAY[27] = 65
DAY[28] = 76
DAY[29] = 55
DAY[30] = 48
DAY[31] = 116
DAY[32] = 79
DAY[33] = 106
DAY[34] = 45
DAY[35] = 54
DAY[36] = 102
DAY[37] = 100
DAY[38] = 65
DAY[39] = 93
DAY[40] = 122
DAY[41] = 84
DAY[42] = 118
DAY[43] = 64
DAY[44] = 103
DAY[45] = 76
DAY[46] = 65
DAY[47] = 109
DAY[48] = 90
DAY[49] = 99
DAY[50] = 69
DAY[51] = 50
DAY[52] = 64
DAY[53] = 61
DAY[54] = 115
DAY[55] = 111
DAY[56] = 64
DAY[57] = 80
DAY[58] = 60
DAY[59] = 68
DAY[60] = 105
DAY[61] = 113
DAY[62] = 84
DAY[63] = 119
DAY[64] = 55
DAY[65] = 77
DAY[66] = 124
DAY[67] = 55
DAY[68] = 115
DAY[69] = 21
DAY[70] = 112
DAY[71] = 41
DAY[72] = 88
DAY[73] = 136
DAY[74] = 66
DAY[75] = 43
DAY[76] = 48
DAY[77] = 55
DAY[78] = 60
DAY[79] = 41
DAY[80] = 43
DAY[81] = 103
DAY[82] = 118
DAY[83] = 19
DAY[84] = 99
DAY[85] = 34
DAY[86] = 118
DAY[87] = 73
DAY[88] = 97
DAY[89] = 74
DAY[90] = 7
DAY[91] = 78
DAY[92] = 60
DAY[93] = 48
DAY[94] = 123
DAY[95] = 125
DAY[96] = 119
DAY[97] = 0
DAY[98] = 36
DAY[99] = 123
DAY[100] = 22


# SageMath 環境で実行

# データ点の設定
points = DAY.items()

# 多項式補間を行う
P = PolynomialRing(GF(p), "x")  # 有理数体上の多項式環を定義
x = P.gen()  # 生成元 x を取得
poly = P.lagrange_polynomial(points)  # ラグランジュ補間を行う

# 補間した多項式を表示
print(poly)

print()
for i in range(101, 133):
    print(chr(poly(i)), end="")

# # 新しい x 座標に対して y 座標を予測
# new_x = 5
# predicted_y = poly(new_x)
# print(f"The predicted y value for x = {new_x} is {predicted_y}.")


# ----------------------------------------

# DAY[101] = ???
# DAY[102] = ???
# DAY[103] = ???
# DAY[104] = ???
# DAY[105] = ???
# DAY[106] = ???
# DAY[107] = ???
# DAY[108] = ???
# DAY[109] = ???
# DAY[110] = ???
# DAY[111] = ???
# DAY[112] = ???
# DAY[113] = ???
# DAY[114] = ???
# DAY[115] = ???
# DAY[116] = ???
# DAY[117] = ???
# DAY[118] = ???
# DAY[119] = ???
# DAY[120] = ???
# DAY[121] = ???
# DAY[122] = ???
# DAY[123] = ???
# DAY[124] = ???
# DAY[125] = ???
# DAY[126] = ???
# DAY[127] = ???
# DAY[128] = ???
# DAY[129] = ???
# DAY[130] = ???
# DAY[131] = ???
# DAY[132] = ???
