def encrypt(plaintext, key):
    key_repeated = (key * (len(plaintext) // len(key))) + key[
        : len(plaintext) % len(key)
    ]
    ciphertext = []
    for p_char, k_char in zip(plaintext.upper(), key_repeated.upper()):
        if p_char.isalpha():
            shift = ord(k_char) - ord("A")
            new_char = chr((ord(p_char) + shift - ord("A")) % 26 + ord("A"))
            ciphertext.append(new_char)
        else:
            ciphertext.append(p_char)
    return "".join(ciphertext)


def decrypt(ciphertext, key):
    key_repeated = (key * (len(ciphertext) // len(key))) + key[
        : len(ciphertext) % len(key)
    ]
    plaintext = []
    for c_char, k_char in zip(ciphertext.upper(), key_repeated.upper()):
        if c_char.isalpha():
            shift = ord(k_char) - ord("A")
            new_char = chr((ord(c_char) - shift - ord("A")) % 26 + ord("A"))
            plaintext.append(new_char)
        else:
            plaintext.append(c_char)
    return "".join(plaintext)
