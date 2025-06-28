from tqdm import trange
from binascii import hexlify
from Crypto.Util.number import long_to_bytes


def FLAG_KILLER(value):
    index = 0
    temp = []
    output = 0
    while value > 0:
        temp.append(2 - (value % 4) if value % 2 != 0 else 0)
        value = (value - temp[index]) / 2
        index += 1
    temp = temp[::-1]
    # print(temp)
    for index in range(len(temp)):
        output += temp[index] * 3 ** (len(temp) - index - 1)
    return output


D = {}
for i in trange(16**3):
    D[int(FLAG_KILLER(i))] = i

enc = "0e98b103240e99c71e320dd330dd430de2629ce326a4a2b6b90cd201030926a090cfc5269f904f740cd1001c290cd10002900cd100ee59269a8269a026a4a2d05a269a82aa850d03a2b6b900883"

pt = ""
for i in range(0, len(enc), 5):
    pt += "%03x" % int(D[int(enc[i : i + 5], 16)])

# 最後の3文字の0埋めが余計なので削除
pt = pt[:-3] + pt[-2:]
print(bytes.fromhex(pt))
