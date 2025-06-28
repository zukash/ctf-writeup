import random


def xor(a: bytes, b: bytes):
    out = []
    for m, n in zip(a, b):
        out.append(m ^ n)
    return bytes(out)


import random


class RNG:
    def __init__(self, size, state=None):
        # 初期化メソッド。sizeは生成する乱数の範囲を決定する。
        self.size = size
        # stateは初期状態を表すリスト。指定がなければ0からsize+1までの範囲をシャッフルしたリストを作成。
        self.state = list(range(self.size + 2))
        random.shuffle(self.state)

    def next(self):
        # sizeのインデックスを取得し、その要素をリストから削除
        idx = self.state.index(self.size)
        self.state.pop(idx)
        # 削除した要素をインデックス+1の位置に挿入
        self.state.insert((idx + 1) % (len(self.state) + 1), self.size)

        # 先頭がsizeなら、先頭を削除して2番目に挿入
        if self.state[0] == self.size:
            self.state.pop(0)
            self.state.insert(1, self.size)

        # size+1のインデックスを取得し、その要素をリストから削除
        idx = self.state.index(self.size + 1)
        self.state.pop(idx)
        # 削除した要素をインデックス+1の位置に挿入
        self.state.insert((idx + 1) % (len(self.state) + 1), self.size + 1)

        # 先頭がsize+1なら、先頭を削除して2番目に挿入
        if self.state[0] == self.size + 1:
            self.state.pop(0)
            self.state.insert(1, self.size + 1)

        # 2番目がsize+1なら、2番目を削除して3番目に挿入
        if self.state[1] == self.size + 1:
            self.state.pop(1)
            self.state.insert(2, self.size + 1)

        # sizeとsize+1のインデックスを取得
        c1 = self.state.index(self.size)
        c2 = self.state.index(self.size + 1)

        # 新しい状態を生成
        self.state = (
            self.state[
                max(c1, c2) + 1 :
            ]  # c1とc2の大きい方の次の要素からリストの最後まで
            + [
                self.size if c1 < c2 else self.size + 1
            ]  # c1がc2より小さい場合はsize、そうでなければsize+1
            + self.state[min(c1, c2) + 1 : max(c1, c2)]  # c1とc2の間の要素
            + [
                self.size if c1 > c2 else self.size + 1
            ]  # c1がc2より大きい場合はsize、そうでなければsize+1
            + self.state[: min(c1, c2)]  # リストの最初からc1とc2の小さい方の要素まで
        )

        # 最後の要素をカウントとして取得
        count = self.state[-1]
        # countがsizeまたはsize+1なら、countをsizeに設定
        if count in [self.size, self.size + 1]:
            count = self.size

        # 新しい状態を生成
        self.state = self.state[count:-1] + self.state[:count] + self.state[-1:]

        # 最初の要素をインデックスとして取得
        idx = self.state[0]
        # インデックスがsizeまたはsize+1なら、インデックスをsizeに設定
        if idx in [self.size, self.size + 1]:
            idx = self.size

        # インデックスに基づいて出力を取得
        out = self.state[idx]
        # 出力がsizeまたはsize+1なら、再帰的にnext()を呼び出して新しい出力を取得
        if out in [self.size, self.size + 1]:
            out = self.next()

        return out


class RNG:
    def __init__(self, size, state=None):
        self.size = size
        self.state = list(range(self.size + 2))
        random.shuffle(self.state)

    def next(self):
        idx = self.state.index(self.size)
        self.state.pop(idx)
        self.state.insert((idx + 1) % (len(self.state) + 1), self.size)
        if self.state[0] == self.size:
            self.state.pop(0)
            self.state.insert(1, self.size)
        idx = self.state.index(self.size + 1)
        self.state.pop(idx)
        self.state.insert((idx + 1) % (len(self.state) + 1), self.size + 1)
        if self.state[0] == self.size + 1:
            self.state.pop(0)
            self.state.insert(1, self.size + 1)
        if self.state[1] == self.size + 1:
            self.state.pop(1)
            self.state.insert(2, self.size + 1)
        c1 = self.state.index(self.size)
        c2 = self.state.index(self.size + 1)
        self.state = (
            self.state[max(c1, c2) + 1 :]
            + [self.size if c1 < c2 else self.size + 1]
            + self.state[min(c1, c2) + 1 : max(c1, c2)]
            + [self.size if c1 > c2 else self.size + 1]
            + self.state[: min(c1, c2)]
        )
        count = self.state[-1]
        if count in [self.size, self.size + 1]:
            count = self.size
        self.state = self.state[count:-1] + self.state[:count] + self.state[-1:]
        idx = self.state[0]
        if idx in [self.size, self.size + 1]:
            idx = self.size
        out = self.state[idx]
        if out in [self.size, self.size + 1]:
            out = self.next()
        return out


i = int(input("got flag? "))
for _ in range(i):
    rng = RNG(128)
    stream = bytes([rng.next() for _ in range(10)])
    print(stream)
