"""
vimjail1
---
vimを操作して、flag.txtを読みに行く。
非想定解が通っていたので、vimjail1.5が公開された。
1.5と1の差分を見てみると、以下が重要っぽいことが分かる。
> inoremap <c-\><c-n> nope

原理は不明だが、<c-\><c-\><c-n>でinsert modeを抜け出せることに気がついた。
normal mode で以下を入力して、フラグを得る。
:e /flag.txt
"""