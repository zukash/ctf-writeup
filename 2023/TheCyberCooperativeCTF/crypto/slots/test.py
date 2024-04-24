import random, time
from randcrack import RandCrack

random.seed(time.time())

rc = RandCrack()

for i in range(624):
	rc.submit(random.getrandbits(32))
	# Could be filled with random.randint(0,4294967294) or random.randrange(0,4294967294)

print("Random result: {}\nCracker result: {}"
	.format(random.randrange(0, 4294967295), rc.predict_randrange(0, 4294967295)))