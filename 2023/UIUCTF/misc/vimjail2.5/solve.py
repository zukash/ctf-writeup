"""
vimjail2.5
---
> cnoremap a _
あたりのmapのせいで、1.5と同様の手法を使えないように思えるが...

https://vim-jp.org/vimdoc-ja/insert.html

> CTRL-Vに続けて、10進数、8進数、16進数のどれかで文字コードを直接入力することが
できる。

これを利用すればよい。

CTRL-R ="\<C-\>\<C-N>"
を順に入力して、insert modeから抜け出すことができた。
"""