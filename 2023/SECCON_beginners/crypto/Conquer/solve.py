from Crypto.Util.number import *
from flag import flag


def ROL(bits, N):
    for _ in range(N):
        bits = ((bits << 1) & (2 ** length - 1)) | (bits >> (length - 1))
    return bits


def encrypt(key, cipher):
    for i in range(32):
        key = ROL(key, pow(cipher, 3, length))
        cipher ^= key
    return key, cipher


def decrypt(key, cipher):
    for i in range(32):
        cipher ^= key
        key = ROL(key, -pow(cipher, 3, length) % length)
    return key, cipher


length = 436
key = 32144306058353820065679430981618262958441561007416241612910091574
cipher = 44511938505668266669058286886369163702114789842616187753983250300
assert (key, cipher) == decrypt(*encrypt(key, cipher))

# lengthで全探索
key = 364765105385226228888267246885507128079813677318333502635464281930855331056070734926401965510936356014326979260977790597194503012948
cipher = 92499232109251162138344223189844914420326826743556872876639400853892198641955596900058352490329330224967987380962193017044830636379
for i in range(1, 1000):
    length = i
    k, c = decrypt(key, cipher)
    flag = long_to_bytes(k ^ c)
    if b"ctf" in flag:
        print(i, flag)
