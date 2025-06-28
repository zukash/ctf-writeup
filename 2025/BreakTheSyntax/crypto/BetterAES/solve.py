"""
AES256の実装です。
一般的なAESの実装と比較して、何かおかしい箇所があれば教えてください。
---
AES-256実装の問題点分析
この実装を一般的なAES-256と比較すると、いくつかの問題点・不自然な点があります：

主な問題点
1. S-boxが単なる連番になっている
実際のAESでは、非線形性を持った置換を行うために複雑なS-boxが使用されます。この実装では単に0から255までの順番の値が入っているため、非線形性がなく安全ではありません。

2. 実装の脆弱性
全て0のブロックを拒否する特殊な制約があり、攻撃のヒントになる可能性があります。通常のAESではこのような制約はありません。

3. 鍵スケジュールの不一致
AES-256の鍵スケジュールでは、32バイトの鍵から60個の32ビットワード（15ラウンド分）を生成しますが、実装上の細かい処理が標準AES-256と異なる箇所があります。

4. パディング方式が非標準
AESでは通常PKCS#7などの標準的なパディングを使用しますが、この実装ではヌルバイトでパディングしています。

5. 暗号モードの問題
ECBモードを使用していますが、同じ平文ブロックが同じ暗号文ブロックになるため安全ではありません。CBC、CTR、GCMなどの安全なモードを使用するのが一般的です。

その他の気になる点
実装が部分的に隠されている可能性があります（添付コードが一部しか見えていないため）

decryptメソッドが実装されていますが、main関数では使用されていません

実際のAESでは、他にも定数が多く使われますが、この実装では非常にシンプル化されています

鍵をユーザーに公開せず、1回限りの暗号化操作（ECBモード）を提供していることから、ECBの弱点を狙った攻撃（オラクル攻撃など）を想定している可能性があります

結論
この「BetterAES」は名前とは裏腹に、標準的なAES-256よりも安全性が低い実装です。特にS-boxが単なる連番であることは、暗号学的強度を大幅に低下させています。このような実装は教育目的や、意図的に弱点を作り出すCTF（Capture The Flag）コンテスト用であると考えられます。
"""

from pwn import *


class BetterAES:
    BLOCK_SIZE = 16  # Block size in bytes
    KEY_SIZE = 32  # Key size in bytes (256 bits)
    NUM_ROUNDS = 14  # Number of rounds for AES-256

    # Round constants
    RCON = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]

    # for easier testing
    sbox = list(range(0, 256))

    def __init__(self, key: bytes):
        self.aes_256_key = key

        # inverse S-box
        self.inv_sbox = [0] * 256
        for i, v in enumerate(self.sbox):
            self.inv_sbox[v] = i

    def gf_mult(self, a, b):
        result = 0
        for _ in range(8):
            if b & 1:
                result ^= a
            high = a & 0x80
            a = (a << 1) & 0xFF
            if high:
                a ^= 0x1B
            b >>= 1
        return result

    def sub_bytes(self, state):
        return [self.sbox[b] for b in state]

    def inv_sub_bytes(self, state):
        return [self.inv_sbox[b] for b in state]

    def shift_rows(self, state):
        new = [0] * 16
        for r in range(4):
            for c in range(4):
                new[r + 4 * c] = state[r + 4 * ((c + r) % 4)]
        return new

    def inv_shift_rows(self, state):
        new = [0] * 16
        for r in range(4):
            for c in range(4):
                new[r + 4 * c] = state[r + 4 * ((c - r) % 4)]
        return new

    def mix_columns(self, state):
        new = state.copy()
        for c in range(4):
            col = state[4 * c : 4 * c + 4]
            new[4 * c + 0] = (
                self.gf_mult(col[0], 2) ^ self.gf_mult(col[1], 3) ^ col[2] ^ col[3]
            )
            new[4 * c + 1] = (
                col[0] ^ self.gf_mult(col[1], 2) ^ self.gf_mult(col[2], 3) ^ col[3]
            )
            new[4 * c + 2] = (
                col[0] ^ col[1] ^ self.gf_mult(col[2], 2) ^ self.gf_mult(col[3], 3)
            )
            new[4 * c + 3] = (
                self.gf_mult(col[0], 3) ^ col[1] ^ col[2] ^ self.gf_mult(col[3], 2)
            )
        return new

    def inv_mix_columns(self, state):
        new = state.copy()
        for c in range(4):
            col = state[4 * c : 4 * c + 4]
            new[4 * c + 0] = (
                self.gf_mult(col[0], 0x0E)
                ^ self.gf_mult(col[1], 0x0B)
                ^ self.gf_mult(col[2], 0x0D)
                ^ self.gf_mult(col[3], 0x09)
            )
            new[4 * c + 1] = (
                self.gf_mult(col[0], 0x09)
                ^ self.gf_mult(col[1], 0x0E)
                ^ self.gf_mult(col[2], 0x0B)
                ^ self.gf_mult(col[3], 0x0D)
            )
            new[4 * c + 2] = (
                self.gf_mult(col[0], 0x0D)
                ^ self.gf_mult(col[1], 0x09)
                ^ self.gf_mult(col[2], 0x0E)
                ^ self.gf_mult(col[3], 0x0B)
            )
            new[4 * c + 3] = (
                self.gf_mult(col[0], 0x0B)
                ^ self.gf_mult(col[1], 0x0D)
                ^ self.gf_mult(col[2], 0x09)
                ^ self.gf_mult(col[3], 0x0E)
            )
        return new

    def add_round_key(self, state, key):
        return [b ^ k for b, k in zip(state, key)]

    def key_expansion(self, key):
        if len(key) != self.KEY_SIZE:
            raise ValueError("Key must be 32 bytes")
        expanded = list(key)
        i = self.KEY_SIZE
        rcon_i = 0
        while len(expanded) < self.BLOCK_SIZE * (self.NUM_ROUNDS + 1):
            temp = expanded[-4:]
            if i % self.KEY_SIZE == 0:
                # RotWord + SubWord + Rcon
                temp = temp[1:] + temp[:1]
                temp = [self.sbox[b] for b in temp]
                temp[0] ^= self.RCON[rcon_i]
                rcon_i += 1
            elif i % self.KEY_SIZE == 16:
                # SubWord only
                temp = [self.sbox[b] for b in temp]
            for j in range(4):
                expanded.append(expanded[i - self.KEY_SIZE + j] ^ temp[j])
            i += 4
        # split into round keys
        return [expanded[16 * r : 16 * (r + 1)] for r in range(self.NUM_ROUNDS + 1)]

    def encrypt_block(self, plaintext):
        key = self.aes_256_key
        if len(plaintext) != self.BLOCK_SIZE or len(key) != self.KEY_SIZE:
            raise ValueError("Plaintext must be 16 bytes and key 32 bytes")
        state = list(plaintext)
        round_keys = self.key_expansion(key)
        state = self.add_round_key(state, round_keys[0])
        for rnd in range(1, self.NUM_ROUNDS):
            state = self.sub_bytes(state)
            state = self.shift_rows(state)
            state = self.mix_columns(state)
            state = self.add_round_key(state, round_keys[rnd])
        state = self.sub_bytes(state)
        state = self.shift_rows(state)
        state = self.add_round_key(state, round_keys[self.NUM_ROUNDS])
        return bytes(state)

    def decrypt_block(self, ciphertext):
        key = self.aes_256_key
        if len(ciphertext) != self.BLOCK_SIZE or len(key) != self.KEY_SIZE:
            raise ValueError("Ciphertext must be 16 bytes and key 32 bytes")
        state = list(ciphertext)
        round_keys = self.key_expansion(key)
        state = self.add_round_key(state, round_keys[self.NUM_ROUNDS])
        for rnd in range(self.NUM_ROUNDS - 1, 0, -1):
            state = self.inv_shift_rows(state)
            state = self.inv_sub_bytes(state)
            state = self.add_round_key(state, round_keys[rnd])
            state = self.inv_mix_columns(state)
        state = self.inv_shift_rows(state)
        state = self.inv_sub_bytes(state)
        state = self.add_round_key(state, round_keys[0])
        return bytes(state)

    def encrypt(self, plaintext: bytes):
        # split to blocks
        blocks = []
        for i in range(0, len(plaintext), self.BLOCK_SIZE):
            blocks.append(plaintext[i : i + self.BLOCK_SIZE])
        # pad
        if blocks:
            blocks[-1] = blocks[-1] + b"\0" * (self.BLOCK_SIZE - len(blocks[-1]))
        # encrypt with ECB
        output = b""
        for block in blocks:
            if block == b"\0" * 16:
                raise Exception(
                    "Wanna encrypt null? What a terrible waste of resources!"
                )
            output += self.encrypt_block(block)
        return output

    def decrypt(self, ciphertext: bytes):
        # split to blocks
        blocks = []
        for i in range(0, len(ciphertext), self.BLOCK_SIZE):
            blocks.append(ciphertext[i : i + self.BLOCK_SIZE])
        # decrypt with ECB
        output = b""
        for block in blocks:
            if block == b"\0" * 16:
                raise Exception(
                    "Wanna decrypt null? What a terrible waste of resources!"
                )
            output += self.decrypt_block(block)
        return output

    def g_block(self, plaintext):
        key = self.aes_256_key
        if len(plaintext) != self.BLOCK_SIZE or len(key) != self.KEY_SIZE:
            raise ValueError("Plaintext must be 16 bytes and key 32 bytes")
        state = list(plaintext)
        round_keys = self.key_expansion(key)
        # state = self.add_round_key(state, round_keys[0])
        for rnd in range(1, self.NUM_ROUNDS):
            # state = self.sub_bytes(state)
            state = self.shift_rows(state)
            state = self.mix_columns(state)
            # state = self.add_round_key(state, round_keys[rnd])
        # state = self.sub_bytes(state)
        state = self.shift_rows(state)
        # state = self.add_round_key(state, round_keys[self.NUM_ROUNDS])
        return bytes(state)

    def g(self, plaintext: bytes):
        # split to blocks
        blocks = []
        for i in range(0, len(plaintext), self.BLOCK_SIZE):
            blocks.append(plaintext[i : i + self.BLOCK_SIZE])
        # pad
        if blocks:
            blocks[-1] = blocks[-1] + b"\0" * (self.BLOCK_SIZE - len(blocks[-1]))
        # encrypt with ECB
        output = b""
        for block in blocks:
            if block == b"\0" * 16:
                raise Exception(
                    "Wanna encrypt null? What a terrible waste of resources!"
                )
            output += self.g_block(block)
        return output

    def g_block_inv(self, ciphertext):
        key = self.aes_256_key
        if len(ciphertext) != self.BLOCK_SIZE or len(key) != self.KEY_SIZE:
            raise ValueError("Ciphertext must be 16 bytes and key 32 bytes")
        state = list(ciphertext)
        round_keys = self.key_expansion(key)
        # state = self.add_round_key(state, round_keys[0])
        for rnd in range(1, self.NUM_ROUNDS):
            # state = self.inv_sub_bytes(state)
            state = self.inv_shift_rows(state)
            state = self.inv_mix_columns(state)
            # state = self.add_round_key(state, round_keys[rnd])
        # state = self.inv_sub_bytes(state)
        state = self.inv_shift_rows(state)
        # state = self.add_round_key(state, round_keys[self.NUM_ROUNDS])
        return bytes(state)

    def g_inv(self, ciphertext: bytes):
        # split to blocks
        blocks = []
        for i in range(0, len(ciphertext), self.BLOCK_SIZE):
            blocks.append(ciphertext[i : i + self.BLOCK_SIZE])
        # pad
        if blocks:
            blocks[-1] = blocks[-1] + b"\0" * (self.BLOCK_SIZE - len(blocks[-1]))
        # encrypt with ECB
        output = b""
        for block in blocks:
            if block == b"\0" * 16:
                raise Exception(
                    "Wanna encrypt null? What a terrible waste of resources!"
                )
            output += self.g_block_inv(block)
        return output


######### test #########
key = b"X" * 32
aes_crypt = BetterAES(key)

pt = (b"\x00" * 15 + b"\x01") + (b"\x01" + b"\x00" * 15)
enc = aes_crypt.encrypt(pt)

print(enc.hex())
assert enc.hex() == "5c4714792370676f2b396b154e1100105e52176a3a71786d2a2c6a0657101f13"

assert pt == aes_crypt.decrypt(enc)
#########################


aes_x = BetterAES(b"X" * 32)
aes_y = BetterAES(b"Y" * 32)

one = b"\x01" * 16
enc_one_x = aes_x.encrypt(one)
enc_one_y = aes_y.encrypt(one)

# two = b"\x02" * 16
two = b"dummy{flag}" + b"AAAAA"
assert len(two) == 16
enc_two_x = aes_x.encrypt(two)
enc_two_y = aes_y.encrypt(two)


assert xor(enc_one_x, enc_two_x) == xor(enc_one_y, enc_two_y)
print(len(enc_one_x))
print(len(enc_two_x))
print(len(enc_one_y))
print(len(enc_two_y))
g_one_g_two = xor(enc_one_x, enc_two_x)

assert aes_x.g(one) == aes_y.g(one)
assert aes_x.g(two) == aes_y.g(two)
assert g_one_g_two == xor(aes_x.g(one), aes_y.g(two))
assert one == aes_x.g_inv(aes_x.g(one))

# これで解ける
g_one = aes_x.g(one)
g_one_g_two = xor(enc_one_x, enc_two_x)
g_two = xor(g_one, g_one_g_two)
assert two == aes_x.g_inv(g_two)

###########################
io = process(
    [
        "openssl",
        "s_client",
        "-connect",
        "betteraes.chal.bts.wh.edu.pl:443",
        "-servername",
        "betteraes.chal.bts.wh.edu.pl",
        "-quiet",
    ]
)
# io = process(["python", "better_aes.py"])

io.recvuntil(b"Flag ciphertext:")
enc_flag = bytes.fromhex(io.recvline().decode().strip())
io.sendlineafter(b"hex form:", one.hex())
io.recvuntil(b"Encrypted:")
enc_one = bytes.fromhex(io.recvline().decode().strip())
g_one = aes_x.g(one)
g_one_g_flag = xor(enc_one, enc_flag)
g_flag = xor(g_one, g_one_g_flag)
print(aes_x.g_inv(g_flag).hex())
print(aes_x.g_inv(g_flag))
