from itertools import groupby
import urllib.parse

from pathlib import Path
from common_variables import CATEGORIES


class Problem:
    def __init__(self, problem, root_dir):
        self.path = problem
        self.problem = (
            f"[{problem.name}]({url_encode(str(problem.relative_to(root_dir)))})"
        )
        self.category = problem.parent.name
        self.contest = problem.parent.parent.name
        self.writeup = "-"
        self.keywords = []
        if problem.joinpath("writeup.md").exists():
            p = url_encode(str(problem.joinpath("writeup.md").relative_to(root_dir)))
            self.writeup = f"[writeup]({p})"


def url_encode(url):
    return urllib.parse.quote(url, safe="/")


def is_valid_year(path):
    return path.is_dir() and path.name.isdigit() and len(path.name) == 4


def get_problems(root_dir):
    for problem in Path(root_dir).glob("**"):
        # 親ディレクトリがカテゴリ名でない場合はスキップ
        if problem.parent.name not in CATEGORIES:
            continue
        # ディレクトリでない場合はスキップ
        if problem.is_file():
            continue
        yield Problem(problem, root_dir)


def generate_table(header, problems):
    """
    header: 表示するカラム
    problems: Problemのリスト
    ---
    問題一覧を Markdown 形式で返す
    """
    table = []
    table.append(" | ".join(header))
    table.append(" | ".join(["---"] * len(header)))
    for problem in problems:
        row = []
        for key in header:
            row.append(str(getattr(problem, key)))
        table.append(" | ".join(row))
    return "\n".join(table)


if __name__ == "__main__":
    root_dir = Path(__file__).parent.parent

    for yyyy in [d for d in root_dir.iterdir() if is_valid_year(d)]:
        # yyyy/README.md 生成
        problems = list(get_problems(yyyy))
        problems.sort(key=lambda x: (x.category, x.contest, x.problem))
        with open(yyyy / "README.md", "w") as f:
            f.write(f"# {yyyy.absolute().name}\n")
            for category, problems in groupby(problems, key=lambda x: x.category):
                f.write(f"\n## {category}\n\n")
                f.write(generate_table(["contest", "problem", "writeup"], problems))
                f.write("\n")

        # yyyy/contest/README.md 生成
        for contest in yyyy.glob("*"):
            problems = list(get_problems(contest))
            if not problems:
                continue
            problems.sort(key=lambda x: (x.category, x.problem))
            with open(contest / "README.md", "w") as f:
                f.write(f"# {contest.name}\n\n")
                f.write(generate_table(["category", "problem", "writeup"], problems))
                f.write("\n")
