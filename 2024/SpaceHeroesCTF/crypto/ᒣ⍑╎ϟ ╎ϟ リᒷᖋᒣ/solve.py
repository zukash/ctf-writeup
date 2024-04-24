from pwn import xor
from Crypto.Cipher import AES

prefix = b"Mortimer_McMire:"
key = b"3153153153153153"
encrypted_flag = bytes.fromhex(open("message.enc").read())

cipher = AES.new(key, AES.MODE_ECB)
iv_xor_prefix = cipher.decrypt(encrypted_flag[:16])
iv = xor(iv_xor_prefix, prefix)


cipher = AES.new(key, AES.MODE_CBC, iv)
pt = cipher.decrypt(encrypted_flag)

print(pt)

# shctf{th1s_was_ju5t_a_big_d1str4ction}