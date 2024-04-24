LOWER_ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def encrypt(secret, key):
    assert len(secret) <= len(key)

    result = ""
    for i in range(len(secret)):
        if (
            secret[i] not in LOWER_ALPHABET
        ):  # Don't encode symbols and capital letters (e.g. "A", " ", "_", "!", "{", "}")
            result += secret[i]
        else:
            result += LOWER_ALPHABET[
                (LOWER_ALPHABET.index(secret[i]) + LOWER_ALPHABET.index(key[i])) % 26
            ]

    return result


flag = input()
key = "thequickbrownfoxjumpsoverthelazydog"
example = "lorem ipsum dolor sit amet"
example_encrypted = encrypt(example, key)
flag_encrypted = encrypt(flag, key)

print(f"{key=}")
print(f"{example=}")
print(f"encrypt(example, key): {example_encrypted}")
print(f"encrypt(flag, key): {flag_encrypted}")

# //////////


def decrypt(secret, key):
    assert len(secret) <= len(key)

    result = ""
    for i in range(len(secret)):
        if (
            secret[i] not in LOWER_ALPHABET
        ):  # Don't encode symbols and capital letters (e.g. "A", " ", "_", "!", "{", "}")
            result += secret[i]
        else:
            result += LOWER_ALPHABET[
                (LOWER_ALPHABET.index(secret[i]) - LOWER_ALPHABET.index(key[i])) % 26
            ]

    return result



print(decrypt(flag_encrypted, key))

print(decrypt("RpgSyk{qsvop_dcr_wmc_rj_rgfxsime!}", key))
