from string import ascii_letters, digits


# こっちだと候補多すぎ
def is_printable(text):
    for t in text:
        if not (32 <= t <= 126):
            return False
        if chr(t) in "{} ()[]|/\\'\"":
            return False
    return True


def is_printable(text):
    for t in text:
        if chr(t) not in ascii_letters + digits + "_!?" + "@#$%&-+=~`":
            return False
    return True


with open("candidates.txt", "rb") as f:
    candidates = f.readlines()

for cand in candidates:
    cand = cand.strip()
    if is_printable(cand) and len(cand) == 32:
        print(cand)
