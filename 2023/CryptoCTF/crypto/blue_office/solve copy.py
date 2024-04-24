from tqdm import tqdm


def reseed(s):
    return s * 214013 + 2531011


def encrypt(s, msg):
    assert s <= 2 ** 32
    c, d = 0, s
    enc, l = b"", len(msg)
    while c < l:
        d = reseed(d)
        enc += (msg[c] ^ ((d >> 16) & 0xFF)).to_bytes(1, "big")
        if c < 5:
            if enc[c] != prefix[c]:
                return b""
        c += 1
    return enc


prefix = "CCTF{"
enc = b"b0cb631639f8a5ab20ff7385926383f89a71bbc4ed2d57142e05f39d434fce"

for s in tqdm(range(2 ** 32 + 1)):
    flag = encrypt(s, enc)
    if b"CCTF" in flag:
        print(flag)
