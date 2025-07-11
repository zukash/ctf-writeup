import json
from Crypto.Hash import CMAC
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15

update_json = {
    "payload": "02a9bae06574e74b0c8afa7839c215a39621428b10d3bff2736493ffb7eeca12b7bb36aee3085e040475faa0d3b3cfac85ed6bedc1caee35ad0ce42c3fa06d42f3224a267d190aada84a3b76807d266ead2b1f5e2eddc3c7772227a4dfbe894bb1d3f47cf4e5aacd653a08c36d57c07c778ab55d9aaba0c99d874eec7ddb8f28",
    "pubkey": "babca97e73b969bd26a13a489f942c508d06774c3f246f7c2e64139932d3ad3276ece5126c4e9e1c5cc541adccf789d47d843d2ea83138810d7ac58da422f23a7e8c5d4a10cf62510eed6c060f9f01087c7ed4ba82ae95a40260b9848a7630f2d2ada3075f656f5e4b56cd94cd3bcd7ee1d8d3427336916b8f4e06207c4577d8f9cfa8bea054c54db5b39fe932d60826fc240235761be17982bb7af46d8a133db836a5b74466b81f13c4be42b76b57c36b8292e509ed35325bceba79591804e084c5caf79c661f22c09a3e5d3da5cb2b64f3e8d451becbe4ff317cf479d475e3bed24c022b3b865d13e8381579ec97ec2e0fe7474cc9db7c8c85036958b77e91",
    "signature": "048a5520c6d1e3859d52056bc6a75fb0d9130cb29abf6bb6d186a6e89d90a2bad67969b5e54a62d80c537bd96accd038e00acd5321be551925972ac82c743a399ef442beca5232bba8dd913c53ba31ffec32b35cc5ec4d9078cae7abfe03081e57db519d9fe7199e6801dfa291fdc32f7fe2c5f79445750bc8c6cd1d0cd4469428d40ba98303005eb058baabd0f25d85a07fb0c5e196e1a5b982cf11f64409d2ab6bf66df4b1e709eb6572149d3316018af73e2cabeed7639e80f6ddc0ed18199e56873fb0cc03dc4e37b02ef8a8557969a8b05f6366c99f36ea05f384a25c81043302c7d296f12b64a43bfc55774bd095dbc529e1a29dcac4fe59b7d51ef83c",
}


def mac(msg):
    cmac = CMAC.new(CMAC_KEY, ciphermod=AES)
    cmac.oid = "2.16.840.1.101.3.4.2.42"
    cmac.update(msg)
    return cmac


def try_read_cmac_key():
    return f"Wasn't easy, but with help from your friend with a scanning electron microscope you managed: {CMAC_KEY.hex()}"


n_bytes = bytes.fromhex(update_json["pubkey"])

FLAG = b"dummy{flag}"
CMAC_KEY = bytes.fromhex("2b7e151628aed2a6abf7158809cf4f3c")
PUBKEY_TAG = mac(n_bytes).digest()
