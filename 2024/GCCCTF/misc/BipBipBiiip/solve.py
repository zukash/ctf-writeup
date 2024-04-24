import re

# 再度必要なライブラリをインポート
import pandas as pd

file_path = "./phonebook.csv"

phonebook = pd.read_csv(file_path)


# 電話番号の形式をチェックする関数
def is_invalid_phone_number(phone_number):
    # 国際電話番号形式または国内電話番号形式にマッチするかどうかをチェック
    if re.match(r"^\+\d[\d\s()]+$", phone_number) or re.match(
        r"^\d{2,4}-\d{1,4}-\d{4}$", phone_number
    ):
        return False
    else:
        return True


# 正しくない形式の電話番号を抽出
invalid_phone_numbers = phonebook[
    phonebook["PHONE_NUMBER"].apply(is_invalid_phone_number)
]

# 抽出した電話番号を表示
invalid = invalid_phone_numbers[["FIRST_NAME", "LAST_NAME", "PHONE_NUMBER"]]
print(invalid)
print(len(invalid))


# 正規表現モジュールをインポート
import re

# 必要なライブラリを再インポートします。
import pandas as pd

# ファイルパス
file_path = "./phonebook.csv"

# CSVファイルを読み込みます。
phonebook = pd.read_csv(file_path)
print(len(phonebook))

# 電話番号の列だけを取得して先頭の数行を表示し、形式を確認します。
phone_numbers = phonebook["PHONE_NUMBER"]
phone_numbers.head(20)


# 分類のための正規表現パターン
patterns = {
    "国際電話番号": r"^\+[0-9\s()]+",
    "国内電話番号（ハイフン区切り）": r"^\d{2,4}-\d{1,4}-\d{4}$",
    "ブロック区切り": r"^\d{2,3}[\s\d]{8,}$",
    "括弧を含む番号": r"^\(\d{3}\)\d{3}-\d{4}$",
    "拡張番号を含む": r"[\dxX]+",
}

# 各分類に対する件数を格納する辞書
counts = {category: 0 for category in patterns}

# 電話番号のリストをループして分類
for phone_number in phone_numbers:
    for category, pattern in patterns.items():
        if re.match(pattern, phone_number):
            counts[category] += 1
            break

# 分類ごとの件数を表示
total = 0
for category, count in counts.items():
    print(f"{category}: {count}")
    total += count
print(total)


# どの分類にも属していないデータを抜き出すための関数
def is_unclassified(phone_number):
    for pattern in patterns.values():
        if re.match(pattern, phone_number):
            return False
    return True


# どの分類にも属していない電話番号を抽出
unclassified_phone_numbers = phone_numbers[phone_numbers.apply(is_unclassified)]

# 抽出した電話番号を表示

print(unclassified_phone_numbers)
print(phonebook[phone_numbers.apply(is_unclassified)])
