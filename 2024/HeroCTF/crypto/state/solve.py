"""
                           ↓ ここを頼りに a1 を見つける
00020ac0: 0000001e0000037f 0000000400000003  ................
00020ad0: 00005afaa168f2a0 00005afaa168f2c0  ..h..Z....h..Z..
00020ae0: 37858f578790fe4a a1de0c5e0b8d8970  J...W..7p...^...
00020af0: 6d2e40924ec1eac0 958e23d9eddc6a48  ...N.@.mHj...#..
00020b00: bdf3302425a56bb3 26ce608a677d04b8  .k.%$0....}g.`.&
00020b10: 817650d0b47314e8 0e0396f64205d2b6  ..s..Pv....B....
00020b20: 18645198cf28082c 6e19ae866cda270d  ,.(..Qd..'.l...n
00020b30: 0fd60a2b45ec00a6 3db5496f84bbe291  ...E+.......oI.=
00020b40: fd1a88be13365644 3cab938047f1c509  DV6........G...<
00020b50: f010bcb111687597 8b7f2039215558c3  .uh......XU!9 ..
00020b60: a0949e1bcdd1d552 3eb21f1eb7a97899  R........x.....>
00020b70: 4c7ba8e166ade5ac 164d17432f1dc7b0  ...f..{L.../C.M.
00020b80: f93f9ca39bd7fb46 e402544182c9a733  F.....?.3...AT..
00020b90: 3a15fa0662ba7a7e 5dc8535b7769349d  ~z.b...:.4iw[S.]
00020ba0: d359b912aaf2eb61 f75f3538dde601df  a.....Y.....85_.
00020bb0: e9e3bfd88c5af8c6 f5f49aefa222af83  ..Z.......".....
00020bc0: ee652dd4ca79db74 cbffe7a45cfce0c2  t.y..-e....\....
00020bd0: 4b63074f1cc47271 7c31323b2acc9f29  qr..O.cK)..*;21|
"""

_a1 = [
    0x37858F578790FE4A,
    0xA1DE0C5E0B8D8970,
    0x6D2E40924EC1EAC0,
    0x958E23D9EDDC6A48,
    0xBDF3302425A56BB3,
    0x26CE608A677D04B8,
    0x817650D0B47314E8,
    0x0E0396F64205D2B6,
    0x18645198CF28082C,
    0x6E19AE866CDA270D,
    0x0FD60A2B45EC00A6,
    0x3DB5496F84BBE291,
    0xFD1A88BE13365644,
    0x3CAB938047F1C509,
    0xF010BCB111687597,
    0x8B7F2039215558C3,
    0xA0949E1BCDD1D552,
    0x3EB21F1EB7A97899,
    0x4C7BA8E166ADE5AC,
    0x164D17432F1DC7B0,
    0xF93F9CA39BD7FB46,
    0xE402544182C9A733,
    0x3A15FA0662BA7A7E,
    0x5DC8535B7769349D,
    0xD359B912AAF2EB61,
    0xF75F3538DDE601DF,
    0xE9E3BFD88C5AF8C6,
    0xF5F49AEFA222AF83,
    0xEE652DD4CA79DB74,
    0xCBFFE7A45CFCE0C2,
    0x4B63074F1CC47271,
    0x7C31323B2ACC9F29,
]

a1 = []
for x in _a1:
    a1.extend([x >> (i * 8) & 0xFF for i in range(8)])

a2 = "ed8cad8dd3853655e490988aedab6e07332aafb1995fe529f6f0d89b82fe"
a2 = [int(a2[i : i + 2], 16) for i in range(0, len(a2), 2)]

print(a1)
print(a2)


def decrypt(a1, a2, v5, v6):
    for i in range(29, -1, -1):
        a2[i] ^= a1[(a1[v5] + a1[v6]) % 256]
        a1[v5], a1[v6] = a1[v6], a1[v5]  # 直接交換
        v6 = (v6 - a1[v5]) % 256
        v5 = (v5 - 1) % 256
    return a2


for v5 in range(256):
    for v6 in range(256):
        flag = decrypt(a1.copy(), a2.copy(), v5, v6)
        if [72, 101, 114, 111, 123] == flag[:5]:
            print(v5, v6)
            print(flag)
            print("".join([chr(c) for c in flag]))
            break

print(decrypt(a1, a2, v5, v6))
