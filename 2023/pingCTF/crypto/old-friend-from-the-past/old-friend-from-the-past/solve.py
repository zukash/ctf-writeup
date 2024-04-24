def is_printable(text):
    for t in text:
        if not (32 <= t <= 126):
            return False
    return True

with open('encrypted_data.bin', 'br') as f:
    enc = f.read()

for d in range(256):
    m = b''
    for e in enc:
        m += chr((e + d) % 256).encode()
    if is_printable(m):
        print(m)

# yrwp{enwr_ermr_erlr_15/03/44_KL}
# http://www.net.c.dendai.ac.jp/crypto/caesar2.html?#
