from typing import Counter
from pwn import *

# 下準備
with open("shrek.txt") as f:
    parts = list(f.read().split())
alphabet = ""
for part in parts:
    for letter in part:
        if not letter in alphabet:
            alphabet += letter
alphabet = alphabet + " "
n = len(alphabet)
print(f'{len(parts) = }')
print(f'{len(alphabet) = }')

def ord(s):
    return alphabet.index(s)

def chr(i):
    return alphabet[i]

while True:
    # 接続
    io = remote('shrek.knping.pl', '50000')
    # io = process(['python', 'main.py'])

    # コーパス収集
    CT_LIST = []
    for _ in range(9):
        io.recvuntil(b'Ciphertext: ')
        CT_LIST.append(io.recvline().decode().strip())
        io.sendline(b'')

    io.recvuntil(b'Ciphertext: ')
    CT_LIST.append(io.recvline().decode().strip())

    # キーの長さは 10 決めうち (1/20)
    K = [None] * 10
    IS = []

    for CT in CT_LIST:
        for i, s in enumerate(CT):
            IS.append((i % 10, s))

    # ' ' の頻度からキーを予測
    for (i, s), _ in Counter(IS).most_common(10):
        print(i, s, _)
        K[i] = (ord(s) - ord(' ')) % n
    if K.count(None) > 0:
        io.close()
        continue

    print(f'{K = }')

    PT = []
    for i, s in enumerate(CT_LIST[-1]):
        pt = chr((ord(s) - K[i % 10]) % n)
        PT.append(pt)

    io.sendline("".join(PT).encode())
    res = io.recvuntil(b'noob')
    if b'ping' in res:
        print(res)
        exit()
