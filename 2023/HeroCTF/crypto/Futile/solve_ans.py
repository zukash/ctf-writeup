from pwn import *
import re
from binascii import unhexlify

context.log_level = 'critical'

# p = remote('static-01.heroctf.fr',9001)
p = process(argv=["python", "chall.py"])


def get_one():
    r = p.recvline().decode().strip()
    p.sendline(b'A')
    return re.findall(r'Hero{(.*?)}',r)[0]

flag = unhexlify(get_one())

all_stat = [[] for k in range(len(flag))]
flag = [0]*len(flag)
charset = [k for k in range(0x00+1,0xff+1)]

while True:
    f = unhexlify(get_one())
    for i in range(len(f)):
        letter = f[i]
        if (letter not in all_stat[i]):
            all_stat[i].append(letter)
        if (len(all_stat[i]) == 255):
            letter = [k for k in charset if k not in all_stat[i]][0]
            flag[i] = letter
            print(bytes(flag))

        know = []
        for k in range(len(all_stat)):
            know.append(len(all_stat[k]))
        print(know)

    if not any([len(x) != 255 for x in all_stat]):
        break

print(flag)
# Hero{Int3rn4l_st4t3s_c4nt_b3_nu77}