from pathlib import Path
from common_variables import CATEGORIES


if __name__ == "__main__":
    contest = Path(input("contest name: "))
    # contest / category 形式でディレクトリ作成
    for category in CATEGORIES:
        (contest / category).mkdir(parents=True)
