# 行列Aを定義
A = Matrix([[2, 3], [4, -1]])

# ベクトルBを定義
B = vector([12, 5])

# 連立方程式を解く
x, y = var("x y")

solution = A.solve_right(B)
print(solution)
