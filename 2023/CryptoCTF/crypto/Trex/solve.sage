from z3 import *

# Z3のソルバーを作成
solver = Solver()

# 変数を定義
x, y, z = Ints("x y z")

# 制約を追加
# equation = And(x != 0, y != 0, z != 0, x ** 2 + y ** 2 - x * y == 568 * z ** 3)
equation = And(x != 0, y != 0, z != 0, x ** 2 + y ** 2 - x * y == 568 * (-1) ** 3)
solver.add(equation)

# 制約を解決
result = solver.check()

# 解の表示
if result == sat:
    model = solver.model()
    x_val = model[x].as_long()
    y_val = model[y].as_long()
    z_val = model[z].as_long()
    print(f"x = {x_val}, y = {y_val}, z = {z_val}")
elif result == unsat:
    print("No solution found.")
else:
    print("Unable to determine satisfiability.")
