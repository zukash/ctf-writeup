import random


class Shrek:
    def __init__(self):
        file = open("shrek.txt")
        self.parts = list(file.read().split())
        alphabet = ""
        for part in self.parts:
            for letter in part:
                if not letter in alphabet:
                    alphabet += letter
        self.alphabet = alphabet + " "
        print(len(alphabet))
        print(len(self.parts))
        self.generateKeys()


    def generateKeys(self):
        keys = []
        for _ in range(20):
            key = []
            # 長さ 10 固定なら解けるか？
            for _ in range(random.randint(10, 30)):
            # for _ in range(random.randint(10, 11)):
                key.append(random.randrange(len(self.alphabet)))
            keys.append(key)

        self.keys = keys


    def generatePlainText(self):
        plainText = ""
        # 長さが増えたら？
        for _ in range(100):
        # for _ in range(1000):
            plainText += random.choice(self.parts)
            plainText += " "
        return plainText.strip()


    def encrypt(self, plainText):
        cipherText = [*plainText]
        for i,j in enumerate(cipherText):
            # # 何も変換されない場合
            # if True:
            #     continue
            # # スペースが変換されない場合は解けるか？
            # if j == " ":
            #     continue

            for key in self.keys:
                cipherText[i] = self.alphabet[(self.alphabet.index(j) + key[i % len(key)]) % len(self.alphabet)]

        ############ keys[-1] しか使ってない ############
        # cipherText2 = [*plainText]
        # for i,j in enumerate(cipherText2):
        #     for key in self.keys[-1:]:
        #         cipherText2[i] = self.alphabet[(self.alphabet.index(j) + key[i % len(key)]) % len(self.alphabet)]
        # assert cipherText == cipherText2
        ###############################################


        return ''.join(cipherText)
