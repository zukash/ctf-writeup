import time

seed = int(time.time() * 1000) % (10**6)


def get_random_number():
    global seed
    print(seed)
    seed = int(str(seed * seed).zfill(12)[3:9])
    return seed


def encrypt(message):
    key = b""
    for i in range(8):
        key += (get_random_number() % (2**16)).to_bytes(2, "big")
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(message, AES.block_size))
    return ciphertext.hex()


print(get_random_number())
print(get_random_number())
print(get_random_number())
print(get_random_number())
print(get_random_number())
print(get_random_number())
