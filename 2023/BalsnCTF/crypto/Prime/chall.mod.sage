import gmpy2
import random

import tqdm
from secret import FLAG

def main():
	n = int(input("prime: "))

	if n <= 0:
		print("No mystiz trick")
	elif n.bit_length() < 256 or n.bit_length() > 512:
		print("Not in range")
	elif not my_is_prime(n):
		print("Not prime")
	else:
		x = int(input("factor: "))

		if x > 1 and x < n and n % x == 0:
			print("You got me")
			print(FLAG)
		else:
			print("gg")

def my_is_prime(n):
	# check if n = a^b for some a, b > 1
	for i in range(2, n.bit_length()):
		root, is_exact = gmpy2.iroot(n, i)
		if is_exact:
			return False

	rs = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
	print(list(test(n, r) for r in rs))
	return all(test(n, r) for r in rs)

def test(n, r):
	"""
	check whether `(x + a) ^ n = x ^ n + a (mod x ^ r - 1)` in Z/nZ for some `a`.
	"""
	R.<x> = Zmod(n)[]
	S = R.quotient_ring(x ^ r - 1)

	a = 1 + random.getrandbits(8)
	if S(x + a) ^ n != S(x ^ (n % r)) + a:
		return False
	return True


# S = set(range(100000))
# for _ in range(10):
# 	S_ = set()
# 	for n in range(10000):
# 		if test(n, 5) and not is_prime(n):
# 			S_.add(n)
# 	S &= S_
# 	print(S)
rs = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# rs = Primes()[:43]

n = 267941267750450995260025669766977699054840704732469037817595358271558392239170103831553042227376417385032303012637531
# n = eval("*".join(map(str, rs)))
# print(my_is_prime(n))

# m = n * 100 + 1
m = n
print(m.bit_length())

for r in rs:
	if pow(r, m, m) != r:
		break
else:
	print("YES")
print(my_is_prime(m))

# for i in range(1, 1000):
# 	rs = Primes()[:i]
# 	n = eval("*".join(map(str, rs)))
# 	m = n + 1
# 	if m.bit_length() > 512:
# 		break
# 	if is_prime(m):
# 		continue
# 	# print(m)
# 	for r in rs:
# 		if pow(r, m, m) != r:
# 			break
# 	else:
# 		print(f"YES {i}")

for k in range(1 << 90, 1 << 91):
	if is_prime(6 * k + 1) and is_prime(12 * k + 1) and is_prime(18 * k + 1):
		print(k)
		n = (6 * k + 1) * (12 * k + 1) * (18 * k + 1)
		for r in rs:
			if pow(r, n, n) != r:
				break
		else:
			print("YES")
		print(my_is_prime(m))
		# my_is_prime(n)

# for i in range(100000):
# 	m = n * i + 1
# 	if is_prime(m):
# 		continue
# 	for r in rs:
# 		if pow(r, m, m) != r:
# 			break
# 	else:
# 		print(f"YES {i}")


# n = 1713045574801
# n = 8911
# n = 1713045574801
# my_is_prime(n)
# # n = 7 * 13 * 19
# # n = 7 * 19 * 67
# r = 3
# R.<x> = Zmod(n)[]
# S = R.quotient_ring(x ^ r - 1)

# a = 1 + random.getrandbits(8)
# print(S(x + a))
# print(S(x + a) ^ (n - 1))
# print(S(x + a) ^ n)

# print(S(x + a) ^ 1)
# print(S(x + a) ^ 2)

# # n = 7 * 13 * 19
# for a in range(1 << 8):
# 	assert S(x + a) ^ n == S(x ^ (n % r)) + a
# 	assert S(x + a) ^ n == S(x) + a
# 	assert pow(a + 1, n, n) == (a + 1)
# 	# assert pow(a + 1, n - 1, n) == 1


# for n in range(1000):
# 	print(n, S(x + a) ^ n)

# T = S(x + a) ^ n


# print(T)
# print(multiplicative_order(T))

"""
3: {1, 1729, 2821, 8911}

"""

# # print(my_is_prime(2305567963945518424753102147331756070))
# while True:
# 	x = random.randint(1 << 256, 1 << 512)
# 	if is_prime(x):
# 		continue
# 	print(x)
# 	if my_is_prime(x):
# 		print(f'OK: {x}')
# 		exit()

