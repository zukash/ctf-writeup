from Crypto.Util.number import getPrime
import secrets

salt = bytes_to_long(secrets.token_bytes(8))

p = getPrime(512)
print(p)

# b0 := bake(m, p - 1, p)
# b1 := bake(m, p - 2, p)

def bake(m, g, p):
    x = m ^^ salt
    return pow(x * g ** 3, m + g * 3, p) + g * x ** 3 % p


def bake(meat: int, g: int, p: int):
    baked = (
        pow((meat ^ salt) * g ** pepper, meat + g * pepper, p)
        + g * (meat ^ salt) ** pepper
    ) % p
    return baked
