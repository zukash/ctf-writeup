import itertools
import random
import base64
import hashlib
from base64 import b64decode


def make_shuffle_list(m):
    num = []
    for i in range(len(m) // 3):
        num.append(i)

    return list(itertools.permutations(num, len(m) // 3))

def make_str_blocks(m):
    tmp = ""
    ret = []
    for i in range(len(m)):
        tmp += m[i]
        if i % 3 == 2:
            ret.append(tmp)
            tmp = ""
    return ret

def unpad(m):
    ret = ""
    for i in range(len(m)):
        ret += m[i]
        if i % 2:
            ret += chr(random.randrange(33, 126))

    while len(ret) % 3:
        ret += chr(random.randrange(33, 126))
    return ret


cipher = b'fWQobGVxRkxUZmZ8NjQsaHUhe3NAQUch'
padflag = b64decode(cipher).decode()
print(padflag)
str_blocks = make_str_blocks(padflag)
print(str_blocks)
for i in range(len(str_blocks)):
    str_blocks[i] = str_blocks[i][:2]

shuffle_list = make_shuffle_list(padflag)

for order in range(len(shuffle_list)):
    flag = ""
    for i in shuffle_list[order]:
        flag += str_blocks[i]
    # print(flag)
    for _ in range(3):
        if (hashlib.sha256(flag.encode()).hexdigest() == "19b0e576b3457edfd86be9087b5880b6d6fac8c40ebd3d1f57ca86130b230222"):
            print(flag)
            print('hoge')
            exit()
        flag = flag[:-1]
