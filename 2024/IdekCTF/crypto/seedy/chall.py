import random, os

flag = (
    os.urandom(random.randrange(0, 1337))
    + open("flag.txt", "rb").read()
    + os.urandom(random.randrange(0, 1337))
)
random.seed(flag)
print(
    len(flag) < 1337 * 1.337
    and "".join(
        map(
            str,
            [random.getrandbits(int(1.337)) for _ in range(int(1337**1.337 * 1.337))],
        )
    )
)
