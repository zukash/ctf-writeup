from Crypto.Cipher import AES
from secret import key, FLAG

p = 4170887899225220949299992515778389605737976266979828742347


def crack_safe(key):
    print(f'{int.from_bytes(key, "big"):0220b}')
    print(f'{int.from_bytes(key, "little"):0220b}')
    print(p)
    return (
        pow(7, int.from_bytes(key, "big"), p)
        == 4118647916916386882780498772489142305911010811458739464304
    )


print(pow(7, int.from_bytes(key, "big"), p))

ct = AES.new(key, AES.MODE_ECB).encrypt(FLAG)
assert crack_safe(key) and AES.new(key, AES.MODE_ECB).decrypt(ct) == FLAG
print(AES.new(key, AES.MODE_ECB).decrypt(ct))
print(FLAG)
