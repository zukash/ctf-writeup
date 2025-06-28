import dis
import opcode


def f():
    len("a")
    pass


# 関数のバイトコードを表示

dis.dis(f)

print(f.__code__.co_names)
print(f.__code__.co_code)


import dis

T = set(opcode.opmap.values())


# 全てのオペコードとその名前を表示
S = set()
for opname, opcode in sorted(dis.opmap.items(), key=lambda item: item[1]):
    S.add(opcode)


print(S - T)
print(T - S)
print(S == T)
