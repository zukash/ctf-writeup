from pwn import *


def solve_knapsack_problem(A, k):
    n = len(A)
    M = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        M[i][i] = 1
    for i in range(n):
        M[i][-1] = A[i]
    M[-1][-1] = -k

    return matrix(M).LLL()[0]


io = remote("35.224.11.111", "31237")
# io = process(["python", "chall.py"])

for _ in range(100):
    io.recvuntil(b"Stage ")
    io.recvline()
    A = list(map(int, io.recvline().decode().strip().split()))
    A, k = A[:-1], A[-1]

    S = solve_knapsack_problem(A, k)[:-1]
    X = []
    S = [i for i, s in enumerate(S) if s == 1]
    print(S)
    io.sendline(" ".join(map(str, S)).encode())
    print(io.recvline())

io.interactive()
