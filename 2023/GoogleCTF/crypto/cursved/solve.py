from hashlib import sha256
from os import urandom


def bytes_to_hexstr(buf):
    return "".join(["{0:02X}".format(b) for b in buf])


def bytes_to_int(buf):
    return int(bytes_to_hexstr(buf), 16)


def random_int(n):
    return bytes_to_int(urandom(n))


def sha256_as_int(x):
    return int(sha256(x).hexdigest(), 16)


def check_type(x, types):
    if len(x) != len(types):
        return False
    for a, b in zip(x, types):
        if not isinstance(a, b):
            return False
    return True


class Curve:
    def __init__(self, p, D, n):
        self.p = p
        self.D = D
        self.n = n

    def __repr__(self):
        return f"Curve(0x{self.p:X}, 0x{self.D:X})"

    def __eq__(self, other):
        return self.p == other.p and self.D == other.D

    def __matmul__(self, other):
        assert check_type(other, (int, int))
        assert other[0] ** 2 % self.p == (self.D * other[1] ** 2 + 1) % self.p
        return Point(self, *other)


class Point:
    def __init__(self, C, x, y):
        assert isinstance(C, Curve)
        self.C = C
        self.x = x
        self.y = y

    def __repr__(self):
        return f"(0x{self.x:X}, 0x{self.y:X})"

    def __eq__(self, other):
        assert self.C == other.C
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        assert self.C == other.C
        x0, y0 = self.x, self.y
        x1, y1 = other.x, other.y
        return Point(
            self.C,
            (x0 * x1 + self.C.D * y0 * y1) % self.C.p,
            (x0 * y1 + x1 * y0) % self.C.p,
        )

    def __rmul__(self, n):
        assert check_type((n,), (int,))
        P = self.C @ (1, 0)
        Q = self
        while n:
            if n & 1:
                P = P + Q
            Q = Q + Q
            n >>= 1
        return P

    def to_bytes(self):
        l = len(hex(self.C.p)[2:])
        return self.x.to_bytes(l, "big") + self.y.to_bytes(l, "big")


C = Curve(
    0x34096DC6CE88B7D7CB09DE1FEC1EDF9B448D4BE9E341A9F6DC696EF4E4E213B3,
    0x3,
    0x34096DC6CE88B7D7CB09DE1FEC1EDF9B448D4BE9E341A9F6DC696EF4E4E213B2,
)
G = C @ (0x2, 0x1)

print(2 * G)
print(C.p * G)
print((C.p + 1) * G)

inv3 = pow(3, -1, C.p - 1)

print(inv3 * (3 * G))
print(inv3 * G)


# S = []
# for i in range(100000):
#     iG = i * G
#     S.append((iG.x, iG.y))

# print(len(set(S)))

# R = C @ (0x1, 0x0)

# def sign(self, m):
#     r = random_int(16) % self.G.C.n
#     R = r * self.G
#     e = sha256_as_int(R.to_bytes() + self.P.to_bytes() + m) % self.G.C.n
#     return (R, (r + self.k * e) % self.G.C.n)
