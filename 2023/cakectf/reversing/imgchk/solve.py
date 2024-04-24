# width = 480
# S = [w + (w >> 3) for w in range(width)]
# T = set(range(max(S))) - set(S)
# print(sorted(T))
from tqdm import trange

height = 20
w = 0
for bit in trange(1 << height):
    image = [(bit >> i & 1) * 255 for i in range(height)]
    a = [0, 0, 0]
    for h in range(height): # 20
        # もしかしたら
        # val = image[h, w] + (w << 3)
        val = image[h]
        # vv = w >> 0x1F
        # v2 = val >> (7 - ((w + (vv >> 5) & 7) - (vv >> 5)) & 0x1F) & 1
        v2 = (val >> (7 - (w & 0x7))) & 1
        a[h >> 3] = a[h >> 3] | (v2 << (h & 7))
    if a == [3, 4, 12]:
        print(image)

