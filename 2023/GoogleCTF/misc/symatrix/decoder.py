import binascii
from random import randint

from Crypto.Util.number import long_to_bytes
from PIL import Image


def hexstr_to_binstr(hexstr):
    n = int(hexstr, 16)
    bstr = ""  # <<<<<<<<<<<<<<
    while n > 0:
        bstr = str(n % 2) + bstr
        n = n >> 1
    if len(bstr) % 8 != 0:
        bstr = "0" + bstr
    return bstr


def pixel_bit(b):  # <<<<<<<<<<<<<<
    return tuple((0, 1, b))


def embed(t1, t2):  # <<<<<<<<<<<<<<
    return tuple((t1[0] + t2[0], t1[1] + t2[1], t1[2] + t2[2]))


def full_pixel(pixel):  # <<<<<<<<<<<<<<
    return pixel[1] == 255 or pixel[2] == 255


print("Embedding file...")

image = Image.open("symatrix.png")
data_to_hide = "deadbeef1234"

w, h = image.size

matrix = image.load()
binary_string = hexstr_to_binstr(data_to_hide)
next_position = 0

print(binary_string)

M = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        M[i][j] = matrix[j, i]

ans = []
for i in range(h):
    for j in range(w // 2):
        if M[i][j] != M[i][~j]:
            l0, l1, l2 = M[i][j]
            r0, r1, r2 = M[i][~j]
            ans.append(r2 - l2)

# assert binary_string == "".join(map(str, ans))

flag = "".join(map(str, ans))
flag = int(flag, 2)
print(long_to_bytes(flag))
flag = hex(flag)
print(flag)

image.close()
