from tqdm import trange
from pwn import *

io = remote("mathgolf.chal-kalmarc.tf", "3470")


def get_irreducible_poly(p):
    Fp = GF(p)
    RFp = PolynomialRing(Fp, ["t"])
    while True:
        poly = [randint(1, p - 1) for _ in range(2)]
        if RFp(poly + [1]).is_irreducible():
            return poly


for _ in trange(100):
    # *********************************************
    # データ入力
    # *********************************************
    io.recvuntil(b"b  = ")
    b = int(io.recvline(), 16)
    io.recvuntil(b"c  = ")
    c = int(io.recvline(), 16)
    io.recvuntil(b"a0 = ")
    a0 = int(io.recvline(), 16)
    io.recvuntil(b"a1 = ")
    a1 = int(io.recvline(), 16)
    io.recvuntil(b"p  = ")
    p = int(io.recvline(), 16)

    print(f"{b = }")
    print(f"{c = }")
    print(f"{a0 = }")
    print(f"{a1 = }")
    print(f"{p = }")

    # *********************************************
    # パラメータの計算
    # *********************************************
    Fp = GF(p)
    RFp = PolynomialRing(Fp, ["t"])
    poly = [-(b**2 + 4 * c) % p, 0]

    if RFp(poly + [1]).roots():
        # *** 平方剰余を持つ場合 ***
        poly = get_irreducible_poly(p)
        F = GF(p**2, name="t", modulus=RFp(poly + [1]))

        phi, psi = RFp([-c, -b, 1]).roots()
        phi, psi = F([phi[0]]), F([psi[0]])
    else:
        # *** 平方剰余を持たない場合 ***
        F = GF(p**2, name="t", modulus=RFp(poly + [1]))
        assert F([0, 1]) ** 2 == -poly[0]
        phi = F([b, 1]) / 2
        psi = F([b, -1]) / 2

    # t**2 - b * t - c == 0 の解であること
    assert phi**2 - b * phi - c == 0
    assert psi**2 - b * psi - c == 0

    const_phi = (-a0 * psi + a1) / (phi - psi)
    const_psi = -(a0 * phi - a1) / (phi - psi)

    # *********************************************
    # データ送信
    # *********************************************
    io.recvuntil(b"Polynomial:")
    print(hex(poly[0]).encode())
    io.sendline(hex(poly[0]).encode())
    io.sendline(hex(poly[1]).encode())

    # io.recvuntil(b"phi:")
    io.sendline(hex(phi[0]).encode())
    io.sendline(hex(phi[1]).encode())

    # io.recvuntil(b"psi:")
    io.sendline(hex(psi[0]).encode())
    io.sendline(hex(psi[1]).encode())

    # io.recvuntil(b"const_phi:")
    io.sendline(hex(const_phi[0]).encode())
    io.sendline(hex(const_phi[1]).encode())

    # io.recvuntil(b"const_psi:")
    io.sendline(hex(const_psi[0]).encode())
    io.sendline(hex(const_psi[1]).encode())

io.interactive()
# kalmar{generalized_fibonacci_sequence_in_a_finite_field__did_you_implement_everything_yourself_for_this__for_non-warmup_you_might_have_to}
