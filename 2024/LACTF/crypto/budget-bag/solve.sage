from params import p, s, points


def solve_knapsack_problem(A, k):
    n = len(A)
    M = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        M[i][i] = 1
    for i in range(n):
        M[i][-1] = A[i]
    M[-1][-1] = -k

    return matrix(M).LLL()


n = len(points)
a, b = 0, 0
for i in range(n):
    x, y = points[i]
    assert (y**2 - x**3 - a * x - b) % p == 0

# ArithmeticError: y^2 = x^3 defines a singular curve
# EllipticCurve([0, 0, 0, 0, 0])
# ref. https://furutsuki.hatenablog.com/entry/2021/03/16/095021

points = [x * pow(y, -1, p) % p for x, y in points]
s = s[0] * pow(s[1], -1, p) % p
print(points)
print(s)
A = solve_knapsack_problem(points + [s, p], 0)[1]

flag = ""
for a in A[:-3]:
    flag += chr(-a & 0b11111111)
flag = "lactf{" + flag + "}"

print(flag)
