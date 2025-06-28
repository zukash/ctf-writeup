from string import digits, ascii_letters
from pwn import xor
from itertools import product

hex_data = "434542034a46505a4c516a6a5e496b5b025b5f6a46760a0c420342506846085b6a035f084b616c5f66685f616b535a035f6641035f6b7b5d765348"
cipher_bytes = bytes.fromhex(hex_data)

key_prefix = xor(cipher_bytes, b"squ1rrel{")[:9].decode()

alphabet = ascii_letters + digits + "_"
for key_suffix in product(digits, repeat=4):
    key = key_prefix + "".join(key_suffix)
    flag = xor(cipher_bytes, key.encode()).decode()
    if flag[-1] == "}":
        # squ1rrel{...}
        flag_content = flag[9:-1]
        if all(c in alphabet for c in flag_content):
            print(flag)
