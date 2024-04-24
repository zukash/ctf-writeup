import requests
import tqdm


def encrypt(message):
    res = requests.get(f"https://electronical.chall.pwnoh.io/encrypt?message={message}")
    return res.text


flag = ""
while "bctf" not in flag:
    for c in tqdm.trange(20, 128):
        guess = chr(c) + flag
        ct = encrypt(guess + "\0" * 24)
        if ct[:32] in ct[32:]:
            flag = guess
            print(f"OK: {flag}")
            break

# bctf{1_c4n7_b3l13v3_u_f0und_my_c0d3b00k}
