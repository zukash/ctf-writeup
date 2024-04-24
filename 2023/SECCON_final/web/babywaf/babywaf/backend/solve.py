import json
import requests

# headers = {"Content-Type": "application/json"}
headers = {
    "Content-Type": "text/plain",
    "Content-Encoding": "deflate",
    "content-length": "106",
}

# headers = {"Content-Encoding": "gzip"}
data = json.dumps({"givemelag": "b", "__proto__": {"a": "b"}})
bignum = "9" * 100
data = json.dumps({"a": 10**100})

# data = """
# {"a": {bignum}}
# """
print(data)

res = requests.post("http://localhost:3000", data, headers=headers)
print(res.text)
# print(res.json())
