---
type: writeup
tags:
---

# emoticons

## 要約

適当な英文を入れて同じ変換をして、数字の頻度分析をする。
6 → 7 → 2 → 0 の順で現れていそう。
chr(0x61) == 'a' and chr(0x7a) == 'z' だから、6,7が多い。
chr(0x20) == ' ' なので、20もそこそこ多い。

英文っぽい文字列になったものだけ抜き出して、頻度分析のツールにかけたらそこそこ読める形になった。
<https://quipqiup.com/>

```text
Emoticons/ also known as smileys/ are graphical representations of facial e~pressions used to convey emotions or tone in written communication+ 4hey have become an integral part of online messaging/ social media platforms/ and email correspondence+ Emoticons are formed using a combination of keyboard characters and symbols/ allowing users to e~press their feelings and add nuance to their te~t!based conversations+ ictf}fre|uency8analysis8is8really8fun8rightq 4he primary purpose of emoticons is to enhance digital communication by bridging the gap between written te~t and face!to!face interactions+ 4hey provide a way to convey emotions/ such as happiness/ sadness/ surprise/ or humor/ which can be challenging to e~press solely through words+ For e~ample/ a simple smiley face Z) can denote happiness or friendliness/ while a frowning face Z. can indicate sadness or disappointment+ Emoticons offer a visual shorthand that helps clarify the intended emotional conte~t of a message/ reducing the chances of miscommunication or misunderstandings+ Moreover/ emoticons also contribute to the creation of a more personalized and relatable online environment+ By using emoticons/ individuals can infuse their written messages with personality/ humor/ or sarcasm+ 4his adds depth and richness to conversations/ making them more engaging and enjoyable+ Emoticons serve as a form of nonverbal communication in the digital realm/ providing a way to convey subtle cues and emotional nuances that would typically be e~pressed through facial e~pressions/ gestures/ or tone of voice in face!to!face interactions+ In summary/ emoticons are graphical representations of facial e~pressions that have revolutionized online communication+ 4hey allow individuals to e~press emotions and add conte~t to their written messages/ improving understanding and reducing the risk of miscommunication+ By incorporating emoticons into digital conversations/ people can infuse their te~ts with personality and create a more vibrant and relatable online environment+
```

あとはエスパーした。

## 考察

## 解法
