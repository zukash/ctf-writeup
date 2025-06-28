from Crypto.Cipher import AES
from pwn import *
import json
import os

context.log_level = "debug"

# interact with users


def receive(r):
    res = r.recvline().decode().strip()
    return json.loads(res)


def send(r, target, req):
    j = json.dumps(req, separators=(",", ":"))
    r.sendlineafter(f"🕊️".encode(), f"{target} {j}".encode())


# cryptographic toolbox

P = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF
G = 0x2


def derive_public_key(private_key: int):
    return pow(G, private_key, P)


def derive_session_key(other_public_key: int, self_private_key: int):
    shared_key = pow(other_public_key, self_private_key, P)
    session_key = hashlib.sha256(shared_key.to_bytes(512, "big")).digest()
    return session_key


def encrypt(session_key: bytes, message: bytes) -> str:
    nonce = os.urandom(8)
    cipher = AES.new(session_key, AES.MODE_CTR, nonce=nonce)
    ciphertext = nonce + cipher.encrypt(message)
    return ciphertext.hex()


def decrypt(session_key: bytes, ciphertext: str) -> bytes:
    ciphertext = bytes.fromhex(ciphertext)
    nonce, ciphertext = ciphertext[:8], ciphertext[8:]
    cipher = AES.new(session_key, AES.MODE_CTR, nonce=nonce)
    return cipher.decrypt(ciphertext)


# ===


def connect():
    return remote("c24a-pigeon-1.hkcert24.pwnable.hk", 1337, ssl=True)


def experiment1():
    r = connect()

    # Alice runs `init_handshake`
    j = receive(r)
    print(f"Alice->Byron: {j}")

    send(r, "byron", j)

    # Byron runs `receive_handshake`
    j = receive(r)
    print(f"Byron->Alice: {j}")

    send(r, "alice", j)

    # Alice runs `finish_handshake`
    j = receive(r)
    print(f"Alice->Byron: {j}")

    send(r, "byron", j)

    # Byron receives the message "done!"
    j = receive(r)
    print(f"Byron->Alice: {j}")

    send(r, "alice", j)

    # Alice receives the message "what is the flag?"
    j = receive(r)
    print(f"Alice->Byron: {j}")

    send(r, "byron", j)

    # Byron receives the message "the flag is..."
    j = receive(r)
    print(f"Byron->Alice: {j}")

    send(r, "alice", j)

    # Alice receives the message "nice flag!"
    j = receive(r)
    print(f"Alice->Byron: {j}")

    send(r, "byron", j)

    # Byron receives the message ":)"


def experiment2():
    r = connect()
    pigeon_private_key = 1337

    # Alice runs `init_handshake`
    j = receive(r)

    # 😈 Before we are sending the message to Byron, we will replace Alice's public key to our own public key
    alice_public_key = j["public_key"]
    pigeon_public_key = derive_public_key(pigeon_private_key)
    j["public_key"] = pigeon_public_key
    send(r, "byron", j)

    # Byron runs `receive_handshake`
    j = receive(r)

    # 😈 TODO: Before we are sending the message back to Alice, we will replace Bob's public key...
    byron_public_key = j["public_key"]
    j["public_key"] = pigeon_public_key
    send(r, "alice", j)

    # Alice runs `finish_handshake`
    j = receive(r)

    # 😈 We need to fix the ciphertext before sending to Byron
    alice_session_key = derive_session_key(alice_public_key, pigeon_private_key)
    m = decrypt(alice_session_key, j["ciphertext"])
    print(f"Alice->Byron: {m}")
    assert m == b"done!", "Did you replace Bob's key with ours?"
    # 😈 TODO: derive the session key between us and Byron, too!
    byron_session_key = derive_session_key(byron_public_key, pigeon_private_key)
    j["ciphertext"] = encrypt(byron_session_key, m)
    send(r, "byron", j)

    # Byron receives the message "done!"
    j = receive(r)
    m = decrypt(byron_session_key, j["ciphertext"])
    print(f"Byron->Alice: {m}")
    j["ciphertext"] = encrypt(alice_session_key, m)
    send(r, "alice", j)

    # 😈 TODO: continue the communication to get the flag!
    j = receive(r)
    m = decrypt(alice_session_key, j["ciphertext"])
    print(f"Alice->Byron: {m}")


if __name__ == "__main__":
    # experiment1()
    experiment2()
