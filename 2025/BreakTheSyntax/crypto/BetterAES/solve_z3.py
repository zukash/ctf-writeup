from z3 import *


class BetterAES:
    BLOCK_SIZE = 16
    KEY_SIZE = 32
    NUM_ROUNDS = 14
    RCON = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]

    def __init__(self, key):
        # BitVecVal 化と key[i] < 256 制約を同時に行う
        self.solver = Solver()
        self.aes_256_key = []
        for k in key:
            if isinstance(k, int):
                bv = BitVecVal(k, 8)
            elif isinstance(k, BitVecRef):
                bv = k
                self.solver.add(ULE(bv, 255))  # key[i] < 256
            else:
                raise TypeError("Invalid key element type")
            self.aes_256_key.append(bv)

    def is_symbolic(self, x):
        return isinstance(x, ExprRef)

    def gf_mult(self, a, b):
        if b == 1:
            return a
        elif b == 2:
            if self.is_symbolic(a):
                high_bit = Extract(7, 7, a) == 1
                result = (a << 1) & 0xFF
                return If(high_bit, result ^ 0x1B, result)
            else:
                result = (a << 1) & 0xFF
                return result ^ 0x1B if a & 0x80 else result
        elif b == 3:
            return self.gf_mult(a, 2) ^ a
        else:
            raise ValueError(f"Unsupported multiplier: {b}")

    def shift_rows(self, state):
        new = [0] * 16
        for r in range(4):
            for c in range(4):
                new[r + 4 * c] = state[r + 4 * ((c + r) % 4)]
        return new

    def mix_columns(self, state):
        new = [0] * 16
        for c in range(4):
            base = 4 * c
            s0, s1, s2, s3 = state[base : base + 4]
            new[base + 0] = self.gf_mult(s0, 2) ^ self.gf_mult(s1, 3) ^ s2 ^ s3
            new[base + 1] = s0 ^ self.gf_mult(s1, 2) ^ self.gf_mult(s2, 3) ^ s3
            new[base + 2] = s0 ^ s1 ^ self.gf_mult(s2, 2) ^ self.gf_mult(s3, 3)
            new[base + 3] = self.gf_mult(s0, 3) ^ s1 ^ s2 ^ self.gf_mult(s3, 2)
        return new

    def add_round_key(self, state, key):
        return [simplify(a ^ b) for a, b in zip(state, key)]

    def sub_word(self, word):
        return word  # S-box無しは仕様

    def key_expansion(self, key):
        expanded = key[:]
        i = self.KEY_SIZE
        rcon_i = 0
        while len(expanded) < self.BLOCK_SIZE * (self.NUM_ROUNDS + 1):
            temp = expanded[-4:]
            if i % self.KEY_SIZE == 0:
                temp = temp[1:] + temp[:1]  # RotWord
                temp = self.sub_word(temp)
                temp[0] = simplify(temp[0] ^ BitVecVal(self.RCON[rcon_i], 8))
                rcon_i += 1
            elif i % self.KEY_SIZE == 16:
                temp = self.sub_word(temp)
            for j in range(4):
                expanded.append(simplify(expanded[i - self.KEY_SIZE + j] ^ temp[j]))
            i += 4
        return [expanded[16 * r : 16 * (r + 1)] for r in range(self.NUM_ROUNDS + 1)]

    def encrypt_block(self, plaintext):
        key = self.aes_256_key
        state = [BitVecVal(b, 8) if isinstance(b, int) else b for b in plaintext]
        round_keys = self.key_expansion(key)
        state = self.add_round_key(state, round_keys[0])
        for rnd in range(1, self.NUM_ROUNDS):
            state = self.shift_rows(state)
            state = self.mix_columns(state)
            state = self.add_round_key(state, round_keys[rnd])
        state = self.shift_rows(state)
        state = self.add_round_key(state, round_keys[self.NUM_ROUNDS])
        return [simplify(s) for s in state]

    def encrypt(self, plaintext: bytes):
        blocks = []
        for i in range(0, len(plaintext), self.BLOCK_SIZE):
            blocks.append(plaintext[i : i + self.BLOCK_SIZE])
        if blocks:
            blocks[-1] = blocks[-1] + b"\0" * (self.BLOCK_SIZE - len(blocks[-1]))
        output = []
        for block in blocks:
            if block == b"\0" * 16:
                raise Exception(
                    "Wanna encrypt null? What a terrible waste of resources!"
                )
            result = self.encrypt_block(list(block))
            output.extend(result)
        return output


# key = b"X" * 32
# aes_crypt = BetterAES(list(key))

pt = (b"\x00" * 15 + b"\x01") + (b"\x01" + b"\x00" * 15)
# enc = aes_crypt.encrypt(pt)

# print(enc)

# assert (
#     bytes(enc).hex()
#     == "5c4714792370676f2b396b154e1100105e52176a3a71786d2a2c6a0657101f13"
# )

key_bytes = [BitVec(f"key_{i}", 8) for i in range(32)]
z3_aes = BetterAES(key_bytes)
enc_state = z3_aes.encrypt(pt)

# enc_state は 16 個の BitVecExpr からなるリスト
# solver = Solver()
# solver = Tactic("simplify").solver()

# 5c4714792370676f2b396b154e1100105e52176a3a71786d2a2c6a0657101f13
z3_aes.solver.add(
    enc_state[0] == 0x5C,
    enc_state[1] == 0x47,
    enc_state[2] == 0x14,
    enc_state[3] == 0x79,
    enc_state[4] == 0x23,
    enc_state[5] == 0x70,
    enc_state[6] == 0x67,
    enc_state[7] == 0x6F,
    enc_state[8] == 0x2B,
    enc_state[9] == 0x39,
    enc_state[10] == 0x6B,
    enc_state[11] == 0x15,
    enc_state[12] == 0x4E,
    enc_state[13] == 0x11,
    enc_state[14] == 0x00,
    enc_state[15] == 0x10,
    enc_state[16] == 0x5E,
    enc_state[17] == 0x52,
    enc_state[18] == 0x17,
    enc_state[19] == 0x6A,
    enc_state[20] == 0x3A,
    enc_state[21] == 0x71,
    enc_state[22] == 0x78,
    enc_state[23] == 0x6D,
    enc_state[24] == 0x2A,
    enc_state[25] == 0x2C,
    enc_state[26] == 0x6A,
    enc_state[27] == 0x06,
    enc_state[28] == 0x57,
    enc_state[29] == 0x10,
    enc_state[30] == 0x1F,
    enc_state[31] == 0x13,
)

# for debug
z3_aes.solver.add(
    key_bytes[0] == 0x58,
    key_bytes[1] == 0x58,
    key_bytes[2] == 0x58,
    key_bytes[3] == 0x58,
    key_bytes[4] == 0x58,
    key_bytes[5] == 0x58,
    key_bytes[6] == 0x58,
    key_bytes[7] == 0x58,
    key_bytes[8] == 0x58,
    key_bytes[9] == 0x58,
    key_bytes[10] == 0x58,
    key_bytes[11] == 0x58,
    key_bytes[12] == 0x58,
    key_bytes[13] == 0x58,
    key_bytes[14] == 0x58,
    key_bytes[15] == 0x58,
    key_bytes[16] == 0x58,
    key_bytes[17] == 0x58,
    key_bytes[18] == 0x58,
    key_bytes[19] == 0x58,
    key_bytes[20] == 0x58,
    key_bytes[21] == 0x58,
    key_bytes[22] == 0x58,
    key_bytes[23] == 0x58,
    key_bytes[24] == 0x58,
    key_bytes[25] == 0x58,
    key_bytes[26] == 0x58,
    key_bytes[27] == 0x58,
    key_bytes[28] == 0x58,
    key_bytes[29] == 0x58,
    # key_bytes[30] == 0x58,
    # key_bytes[31] == 0x58,
)

print(z3_aes.solver.check())
print(z3_aes.solver.model())
