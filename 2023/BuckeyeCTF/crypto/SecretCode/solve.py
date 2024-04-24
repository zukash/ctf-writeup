# from pwn import *

# ct = "1:10:d0:10:42:41:34:20:b5:40:03:30:91:c5:e1:e3:d2:a2:72:d1:61:d0:10:e3:a0:43:c1:01:10:b1:b1:b0:b1:40:9"
# # ct = "".join([chr(int(c, 16)) for c in ct.split(b":")])
# key = xor("bctf{", ct[:5])
# print(key)
# print(xor(key, ct))
# # for c in range(256):
# #     pt = xor(chr(c), ct)
# #     print(pt)


encrypted_flag = "1:10:d0:10:42:41:34:20:b5:40:03:30:91:c5:e1:e3:d2:a2:72:d1:61:d0:10:e3:a0:43:c1:01:10:b1:b1:b0:b1:40:9"
xor_key = "snub_wrestle"

# 文字列を16進数のバイト列に変換
flag_bytes = bytes.fromhex(encrypted_flag.replace(":", ""))

# XOR鍵をバイト列に変換
key_bytes = bytes(xor_key, "utf-8")

# フラグをXOR復号
decrypted_flag_bytes = bytes(
    x ^ key_bytes[i % len(key_bytes)] for i, x in enumerate(flag_bytes)
)

# 復号されたフラグを文字列に変換
decrypted_flag = decrypted_flag_bytes.decode("utf-8")

print("Decrypted Flag:", decrypted_flag)
