from pwn import *


def quaternion2matrix(q):
    a, b, c, d = q
    return matrix(
        Zmod(p),
        [
            [a, b, c, d],
            [-b, a, -d, c],
            [-c, d, a, -b],
            [-d, -c, b, a],
        ],
    )


# 333-bit unsafe prime
p = 11321863774154065493669429802057244089485780539517486784165951867921444011145408000000000000000000001
assert p.is_prime()
assert p.bit_length() == 333
print(factor(p - 1))


def solve():
    # io = process(["sage", "problem.sage"])
    io = remote("dlp-4-0.dom.seccon.games", "8888")

    io.recvuntil(b"p:")
    io.sendline(str(p).encode())

    i, j, k = QuaternionAlgebra(Zmod(p), -1, -1).gens()
    io.recvuntil(b"g = ")
    g = eval(io.recvline())

    io.recvuntil(b"h = ")
    h = eval(io.recvline())

    G = quaternion2matrix(g)
    H = quaternion2matrix(h)

    try:
        B, P = G.diagonalization()
        print(f"{B = }")
        print(f"{P = }")
    except ValueError:
        io.close()
        return b""

    Bk = P.inverse() * H * P

    x = discrete_log(Zmod(p)(Bk[0][0]), Zmod(p)(B[0][0]))
    io.recvuntil(b"x:")
    io.sendline(str(x).encode())
    flag = io.recvline()
    io.close()
    return flag


flag = b""
while b"SECCON" not in flag:
    flag = solve()
    print(flag)

print(flag)
