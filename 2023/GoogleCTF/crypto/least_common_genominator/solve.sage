from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, isPrime, long_to_bytes

with open("public.pem", "r") as pub_file:
    rsa = RSA.import_key(pub_file.read())

print(rsa.n)
print(rsa.e)

S = [
    2166771675595184069339107365908377157701164485820981409993925279512199123418374034275465590004848135946671454084220731645099286746251308323653144363063385,
    6729272950467625456298454678219613090467254824679318993052294587570153424935267364971827277137521929202783621553421958533761123653824135472378133765236115,
    2230396903302352921484704122705539403201050490164649102182798059926343096511158288867301614648471516723052092761312105117735046752506523136197227936190287,
    4578847787736143756850823407168519112175260092601476810539830792656568747136604250146858111418705054138266193348169239751046779010474924367072989895377792,
    7578332979479086546637469036948482551151240099803812235949997147892871097982293017256475189504447955147399405791875395450814297264039908361472603256921612,
    2550420443270381003007873520763042837493244197616666667768397146110589301602119884836605418664463550865399026934848289084292975494312467018767881691302197,
]

print([s.bit_length() for s in S])

n = (S[1] - S[2]) ** 2 - (S[0] - S[1]) * (S[2] - S[3])
for i in range(3):
    n = gcd(n, (S[i + 1] - S[i + 2]) ** 2 - (S[i] - S[i + 1]) * (S[i + 2] - S[i + 3]))

print(n)
print(n.bit_length())

m = pow(S[0] - S[1], -1, n) * (S[1] - S[2]) % n
c = (S[1] - S[0] * m) % n


class LCG:
    lcg_m = m
    lcg_c = c
    lcg_n = n

    def __init__(self, lcg_s):
        self.state = lcg_s

    def next(self):
        self.state = (self.state * self.lcg_m + self.lcg_c) % self.lcg_n
        return self.state


if __name__ == "__main__":
    it = 8
    bits = 512

    # Find prime value of specified bits a specified amount of times
    seed = 211286818345627549183608678726370412218029639873054513839005340650674982169404937862395980568550063504804783328450267566224937880641772833325018028629959635
    lcg = LCG(seed)
    primes_arr = []

    dump = True
    items = 0
    dump_file = open("dump.txt", "w")

    primes_n = 1
    while True:
        for i in range(it):
            while True:
                prime_candidate = lcg.next()
                if dump:
                    dump_file.write(str(prime_candidate) + "\n")
                    items += 1
                    if items == 6:
                        dump = False
                        dump_file.close()
                if not isPrime(prime_candidate):
                    continue
                elif prime_candidate.bit_length() != bits:
                    continue
                else:
                    primes_n *= prime_candidate
                    primes_arr.append(prime_candidate)
                    break

        # Check bit length
        if primes_n.bit_length() > 4096:
            print("bit length", primes_n.bit_length())
            primes_arr.clear()
            primes_n = 1
            continue
        else:
            break

    print(primes_arr)
    n = 1
    for j in primes_arr:
        n *= j
    print("[+] Public Key: ", n)
    print("[+] size: ", n.bit_length(), "bits")

    phi = 1
    for k in primes_arr:
        phi *= k - 1

    # Calculate private key 'd'
    d = pow(rsa.e, -1, phi)

    with open("flag.txt", "rb") as flag_file:
        flag = int.from_bytes(flag_file.read(), "little")
        # flag = bytes_to_long(flag_file.read())

    flag = pow(flag, d, n)
    print(long_to_bytes(flag))
