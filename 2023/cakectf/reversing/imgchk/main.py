for w in range(width): # 480
    a = [0, 0, 0]
    for h in range(height): # 20
        # もしかしたら
        # val = image[h, w] + (w << 3)
        val = image[w + (w >> 3), h]
        # vv = w >> 0x1F
        # v2 = val >> (7 - ((w + (vv >> 5) & 7) - (vv >> 5)) & 0x1F) & 1
        v2 = (val >> (7 - (w & 0x7))) & 1
        a[h >> 3] = a[h >> 3] | (v2 << (h & 7))
    hs = hashlib.md5(bytes(a)).hexdigest()
    if answer[w] != hs:
        print("Invalid flag")
        exit()
