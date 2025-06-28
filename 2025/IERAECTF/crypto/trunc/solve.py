from sage.all import *

q = 2**20
n = 512
m = 4 * n
c = 8
q_ = q // (2**c)

# 1. 出力データの読み込み
import ast

with open("output.txt") as f:
    lines = f.read()
    q = int(lines.split("q = ")[1].split("\n")[0])
    n = int(lines.split("n = ")[1].split("\n")[0])
    m = int(lines.split("m = ")[1].split("\n")[0])
    c = int(lines.split("c = ")[1].split("\n")[0])
    A = ast.literal_eval(lines.split("A = ")[1].split("\n")[0])
    b = ast.literal_eval(lines.split("b = ")[1].split("\n")[0])
    flag_ciphertext = ast.literal_eval(
        lines.split("flag_ciphertext = ")[1].split("\n")[0]
    )


# 2. A, bを256で割る
A_ = Matrix(ZZ, m, n, [[aij // 256 for aij in row] for row in A])
b_ = vector(ZZ, [bi // 256 for bi in b])


# # 3. LWE instance: b_ = A_ * s + e_ (mod q_)
# # ノイズe_は0か1なので格子攻撃が効く

# # Babai's nearest planeでsを推定
# M = A_.augment(identity_matrix(ZZ, m))
# target = b_
# print("Solving the LWE instance...")

# # LLL reduction
# B = M.T
# B = B.LLL()
# s_guess = B.solve_left(target)

# print("LLL reduction completed.")

# # s_guessは連続値なので、四捨五入してmod q_に
# s_vec = vector(ZZ, [int(round(x)) % q_ for x in s_guess[:n]])

# # 4. 復号
# flag_bits = []
# for a_sum, b_sum in flag_ciphertext:
#     # a_sum, b_sumも整数リスト
#     a_sum = vector(ZZ, a_sum)
#     inner = int(a_sum.dot_product(s_vec)) % q
#     val = (b_sum - inner) % q
#     # 0に近ければ0, q//2に近ければ1
#     bit = 1 if abs(val - q // 2) < abs(val) else 0
#     flag_bits.append(bit)

# # 8ビットずつまとめてフラグ復元
# flag_bytes = []
# for i in range(0, len(flag_bits), 8):
#     byte = 0
#     for j in range(8):
#         if i + j < len(flag_bits):
#             byte |= flag_bits[i + j] << j
#     flag_bytes.append(byte)

# flag = bytes(flag_bytes)
# print(flag)
