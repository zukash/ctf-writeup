from unicodedata import numeric

text = "*" * 12345678 + "FAKECTF{THIS_IS_FAKE}" + "*" * 12345678


# I made a simple calculator :)
def calc(s):
    if (loc := s.find("+")) != -1:
        return calc(s[:loc]) + calc(s[loc + 1 :])
    if (loc := s.find("*")) != -1:
        return calc(s[:loc]) * calc(s[loc + 1 :])
    x = 0
    for c in s:
        x = 10 * x + numeric(c)
    return x


def check(s):
    if not all(c.isnumeric() or c in "+*" for c in s):
        return False
    if len(s) >= 6:  # I don't like long expressions!
        return False
    return True


s = input()
if check(s):
    val = int(calc(s))
    print(f"{val} th character is {text[val]}")
else:
    print(":(")

# ༬𞴣༰𒐳㉘
# ①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽⑾⑿⒀⒁⒂⒃⒄⒅⒆⒇⒈⒉⒊⒋⒌⒍⒎⒏⒐⒑⒒⒓⒔⒕⒖⒗⒘⒙⒚⒛⓪⓫⓬⓭⓮⓯⓰⓱⓲⓳⓴⓵⓶⓷⓸⓹⓺⓻⓼⓽⓾⓿❶❷❸❹❺❻❼❽❾❿➀➁➂➃➄➅➆➇➈➉➊➋➌➍➎➏➐➑➒➓⳽〇〡〢〣〤〥〦〧〨〩〸〹〺㆒㆓㆔㆕㈠㈡㈢㈣㈤㈥㈦㈧㈨㈩㉈㉉㉊㉋㉌㉍㉎㉏㉑㉒㉓㉔㉕㉖㉗㉘㉙㉚㉛㉜㉝㉞㉟㊀㊁㊂㊃㊄㊅㊆㊇㊈㊉㊱㊲㊳㊴㊵㊶㊷㊸㊹㊺㊻㊼㊽㊾㊿
