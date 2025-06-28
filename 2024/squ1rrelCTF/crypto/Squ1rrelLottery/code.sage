# GF(2)上の線形コードの構築
F = GF(2)

# [63, 46, 7]の生成多項式
gen_poly = (
    x
    ^ 17 + x
    ^ 16 + x
    ^ 15 + x
    ^ 13 + x
    ^ 12 + x
    ^ 8 + x
    ^ 6 + x
    ^ 4 + x
    ^ 3 + x
    ^ 2 + 1
)

# [63, 46, 7]の循環線形コードの構築
C = codes.CyclicCode(gen_poly, F)

# [64, 46, 8]の線形コードの構築
C_extend = C.extend(1)

# [60, 42, 8]の線形コードの構築
C_shortened = C_extend.shorten([61, 62, 63, 64])

# [60, 40, 8]の線形コードの構築
C_subcode = C_shortened.subcode(
    [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        31,
        32,
        33,
        34,
        35,
        36,
        37,
        38,
        39,
        40,
    ]
)

# 結果の表示
print("Construction of a linear code [60, 40, 8] over GF(2):")
print("[1]:  [63, 46, 7] Cyclic Linear Code over GF(2)")
print(
    "     CyclicCode of length 63 with generating polynomial x^17 + x^16 + x^15 + x^13 + x^12 + x^8 + x^6 + x^4 + x^3 + x^2 + 1"
)
print("[2]:  [64, 46, 8] Linear Code over GF(2)")
print("     ExtendCode [1] by 1")
print("[3]:  [60, 42, 8] Linear Code over GF(2)")
print("     Shortening of [2] at { 61 .. 64 }")
print("[4]:  [60, 40, 8] Linear Code over GF(2)")
print("     Subcode of [3]")
print("\nlast modified: 2001-01-30")
