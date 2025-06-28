from Crypto.Util.number import long_to_bytes
from params import n, ct, signature
from tqdm import trange

e = 65537
# crc_hqx の出力は 16 bit
for d in trange(1, 1 << 16):
    g, a, b = xgcd(e, d)
    assert a * e + b * d == g == 1
    flag = pow(ct, a, n) * pow(signature, b, n) % n
    flag = long_to_bytes(flag)
    if flag.startswith(b"ictf{"):
        print(flag)
        break
