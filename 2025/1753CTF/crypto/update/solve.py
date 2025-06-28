from pwn import *
import json
from Crypto.Hash import CMAC
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Util.number import bytes_to_long, long_to_bytes, size, ceil_div

# FLAG 以外は実質的に公開情報
from secret import mac, CMAC_KEY, PUBKEY_TAG, try_read_cmac_key, update_json


# n_bytes = bytes.fromhex(update_json["pubkey"])
# signature_bytes = bytes.fromhex(update_json["signature"])
# payload_bytes = bytes.fromhex(update_json["payload"])

# n = int.from_bytes(n_bytes, "big")
# e = 0x10001
# pubkey = RSA.construct((n, e))
# verifier = pkcs1_15.new(pubkey)

# io = remote("update-602955aaae93.tcp.1753ctf.com", 16681)
io = process(["python", "update_update.mod.py"])

io.sendlineafter(b"your choice: ", b"2")
io.sendlineafter(b"update package: ", json.dumps(update_json).encode())

# update_json["payload"] = b"Gimmie a flag, pretty please.".hex()
update_json["pubkey"] = b"11".hex()
io.sendlineafter(b"your choice: ", b"2")
io.sendlineafter(b"update package: ", json.dumps(update_json).encode())

io.interactive()
