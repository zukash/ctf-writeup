import pandas as pd
from datetime import datetime

# データベースを読み込む（CSVファイルを想定）
df = pd.read_csv("orders.csv")

print(df)

# 日付を datetime オブジェクトに変換
df["date"] = pd.to_datetime(df["date"])


# 1. 2023-01-01までに最も多くのお金を持っている人を見つける
def find_richest_person(df):
    # 全ユーザーの初期残高を設定
    balance = {
        i: 10000 for i in set(df["buyer_id"].unique()) | set(df["seller_id"].unique())
    }

    # 2023-01-01以前の取引のみを考慮
    df_filtered = df[df["date"] < "2023-01-01"]

    for _, row in df_filtered.iterrows():
        actual_price = row["price"] * (1 - row["discount"] / 100)
        balance[row["buyer_id"]] -= actual_price
        balance[row["seller_id"]] += actual_price

    richest_person = max(balance, key=balance.get)
    return richest_person, balance[richest_person]


# 2. 2023-01-01までの割引による節約額を計算
def calculate_total_discount(df):
    df_filtered = df[df["date"] < "2023-01-01"]
    total_discount = ((df_filtered["price"] * df_filtered["discount"] / 100)).sum()
    return int(total_discount)


# 3. 2023-01-01までに残高がマイナスになった人数を数える
def count_negative_balances(df):
    balance = {
        i: 10000 for i in set(df["buyer_id"].unique()) | set(df["seller_id"].unique())
    }
    df_filtered = df[df["date"] < "2023-01-01"]

    for _, row in df_filtered.iterrows():
        actual_price = row["price"] * (1 - row["discount"] / 100)
        balance[row["buyer_id"]] -= actual_price
        balance[row["seller_id"]] += actual_price

    negative_count = sum(1 for value in balance.values() if value < 0)
    return negative_count


# 結果を出力
richest_person, max_balance = find_richest_person(df)
print(
    f"1. 2023-01-01までに最も多くのお金を持っている人: ID {richest_person}, 残高 ${max_balance:.2f}"
)

total_discount = calculate_total_discount(df)
print(f"2. 2023-01-01までの割引による総節約額: ${total_discount}")

negative_count = count_negative_balances(df)
print(f"3. 2023-01-01までに残高がマイナスになった人数: {negative_count}人")

print(f"{richest_person}_{total_discount}_{negative_count}")
