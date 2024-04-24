from Crypto.PublicKey import RSA
from Crypto.Util.number import *

with open("private.pem", "r") as f:
    private_key = f.read()
with open("public.pem", "r") as f:
    public_key = f.read()
with open("flag.enc", "rb") as f:
    flag_enc = f.read()

private_key = RSA.import_key(private_key)
public_key = RSA.import_key(public_key)

print(private_key)
print(public_key)

flag = pow(bytes_to_long(flag_enc), private_key.d, public_key.n)
print(long_to_bytes(flag))
