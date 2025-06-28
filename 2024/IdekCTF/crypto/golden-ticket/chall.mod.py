from Crypto.Util.number import *


# Some magic from Willy Wonka
def chocolate_generator(m: int) -> int:
    p = 396430433566694153228963024068183195900644000015629930982017434859080008533624204265038366113052353086248115602503012179807206251960510130759852727353283868788493357310003786807
    return (pow(13, m, p) + pow(37, m, p)) % p


# The golden ticket is hiding inside chocolate
flag = b"idek{REDACTED}"
golden_ticket = bytes_to_long(flag)
golden_ticket = 10
print(golden_ticket)
print(chocolate_generator(9))
print(chocolate_generator(10))


flag_chocolate = chocolate_generator(golden_ticket)
print(flag_chocolate)
chocolate_bag = []

# Willy Wonka is making chocolates
for i in range(golden_ticket):
    chocolate_bag.append(chocolate_generator(i))

# And he put the golden ticket at the end
chocolate_bag.append(flag_chocolate)

# Augustus ate lots of chocolates, but he can't eat all cuz he is full now :D
remain = chocolate_bag[-2:]

# Can you help Charles get the golden ticket?
print(remain)

# [88952575866827947965983024351948428571644045481852955585307229868427303211803239917835211249629755846575548754617810635567272526061976590304647326424871380247801316189016325247, 67077340815509559968966395605991498895734870241569147039932716484176494534953008553337442440573747593113271897771706973941604973691227887232994456813209749283078720189994152242]

# h0 = 13 ** (x - 1) + 37 ** (x - 1)
# h1 = 13 ** x + 37 ** x
# h1 - h0 * 13 = 37 ** x - 13 * 37 ** (x - 1) = 24 * 37 ** (x - 1)

p = 396430433566694153228963024068183195900644000015629930982017434859080008533624204265038366113052353086248115602503012179807206251960510130759852727353283868788493357310003786807
h0, h1 = [129972344294450, 4808722230909698]
h = h1 - h0 * 13
print(h)

h = h1 - h0 * 13
h *= pow(24, -1, p)
h %= p
print(pow(37, 9, p) * 24)
assert pow(37, 9, p) == pow(37, 9, p) * 24 * pow(24, -1, p) % p
