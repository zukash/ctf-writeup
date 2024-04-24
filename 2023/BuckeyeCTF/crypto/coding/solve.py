with open("flag.compressed", "rb") as f:
    ct = f.read()
print(ct)
print(len(ct))

import pickle

pickle.loads(ct)

import struct

# バイト列を定義 (例: 4バイトのバイト列)
byte_data = b"\x40\x49\x0f\xdb"

# バイト列を浮動小数点数に変換 (32ビットの浮動小数点数)
float_value = struct.unpack("f", ct)[0]

print(float_value)


# # ASCII文字列 "hoge" の出現頻度が一定と仮定
# symbol_probabilities = {"h": 0.25, "o": 0.25, "g": 0.25, "e": 0.25}


# def arithmetic_encode(input_string, symbol_probabilities):
#     low = 0.0  # 現在の下限
#     high = 1.0  # 現在の上限
#     result = 0.0  # 結果の数値

#     for symbol in input_string:
#         # 現在のシンボルの確率と範囲を取得
#         symbol_probability = symbol_probabilities.get(symbol, 0.0)
#         symbol_range = high - low

#         # 新しい下限と上限を計算
#         high = low + symbol_range * symbol_probability
#         low = low + symbol_range * symbol_probabilities[symbol]

#     result = (low + high) / 2.0  # 結果を平均化

#     return result


# # サンプルとして "hoge" をエンコード
# encoded_value = arithmetic_encode("hoge", symbol_probabilities)
# print(f"Encoded value: {encoded_value:.5f}")
