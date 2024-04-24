from pwn import *

with open('emperors_new_crypto_encrypted.txt') as f:
    CT = f.read().strip().split('\n')
    CT = [bytes.fromhex(ct) for ct in CT]
    
def is_printable(text):
    for t in text:
        if not (32 <= t <= 126):
            return False
    return True

known = b'flag'
# known = b'flag{the_emperors_new_groove_is_his_totally_new_crypto_&_his_fancy_new_clothes!}'
while len(known) < 80:
    for c in range(127):
        predict = known + chr(c).encode()
        P = [xor(ct[:len(predict)], predict) for ct in CT]
        if all(is_printable(p) for p in P):
            print(f'{chr(c)}: {[p.decode() for p in P]}')
            # print(f'=========={c}==========')
            # print(*[p.decode() for p in P], sep='\n')
    print(f'known: {known}')
    c = input().strip()
    known = known + c.encode()
    print(known)

