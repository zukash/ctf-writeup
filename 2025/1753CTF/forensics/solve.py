import struct
import numpy as np

# ファイルパスを指定
file_path = "digital-0.bin"

# サンプリングレート（例: 16MHz）
sample_rate = 16_000_000  # Hz


# バイナリファイルを読み込む関数
def read_binary_file(file_path):
    with open(file_path, "rb") as f:
        # ファイル全体を読み込む
        data = f.read()
        # データを1バイトずつアンパック
        samples = np.frombuffer(data, dtype=np.uint8)
    return samples


# データ解析
def analyze_data(samples, sample_rate):
    print(f"Total Samples: {len(samples)}")
    print(f"Duration: {len(samples) / sample_rate:.6f} seconds")

    # サンプルの一部を表示
    print("First 20 Samples:")
    print(samples[:20])


# メイン処理
if __name__ == "__main__":
    # バイナリデータを読み込み
    samples = read_binary_file(file_path)

    # データを解析
    analyze_data(samples, sample_rate)
