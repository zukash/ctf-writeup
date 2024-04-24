from gost28147 import cbc_decrypt

key = b"SKYSHOCKSKYSHOCKSKYSHOCKSKYSHOCK"
data = open("encrypted.enc", "rb").read()

print(cbc_decrypt(key, data, pad=False))

with open("data", "wb") as f:
    f.write(cbc_decrypt(key, data, pad=False))
