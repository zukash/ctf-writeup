from pwn import *

with open('ciphertext.txt') as f:
    CT = f.read().strip().split('\n')
    CT = [bytes.fromhex(ct) for ct in CT]

def is_printable(text):
    for t in text:
        if not (32 <= t <= 126):
            return False
    return True

# known = b'flag{where_are_elpheba_and_glinda_i_thought_this_was_wicked'
known = b'wicked'
while len(known) < 59:
    for c in range(127):
        predict = chr(c).encode() + known
        P = [xor(ct[-len(predict):], predict) for ct in CT]
        if all(is_printable(p) for p in P):
            print(f'{chr(c)}: {[p.decode() for p in P]}')
            # print(f'=========={c}==========')
            # print(*[p.decode() for p in P], sep='\n')
    print(f'known: {known}')
    c = input().strip()
    known = c.encode() + known
    print(known)


"""
'Now the Wicked Witch of the West had but one eye, yet that '
'was as powerful as a telescope, and could see everywhere.  '
'So, as she sat in the door of her castle, she happened to  '
'look around and saw Dorothy lying asleep, with her friends '
'all about her. They were a long distance off, but the      '
'Wicked Witch was angry to find them in her country; so she '
'blew upon a silver whistle that hung around her neck.      '
"""
