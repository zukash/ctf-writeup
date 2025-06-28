from pwn import *

# context.log_level = "CRITICAL" # minimize logging


def read_hash(idx):
    r = remote("c55-flag-hasher.hkcert24.pwnable.hk", 1337, ssl=True)

    r.recvuntil(
        b"2 - Read Hash record\n"
    )  # wait until we receive this text... which is when we need to response
    r.sendline(b"2")  # and send the command

    r.recvuntil(b"Idx: ")

    r.sendline(str(idx).encode())  # convert `idx` to string, and send it

    try:
        server_response = r.recvline()  # save server response to variable
        print(server_response)

        hex_ouput = server_response.split(b" : ")[
            1
        ]  # get only the hex part out of the server response
        print("Received hex: ", hex_ouput)
    except:
        print("Error reading hash")
    r.close()


# read_hash(1464)
# read_hash(1464 // 8)


r = remote("c55-flag-hasher.hkcert24.pwnable.hk", 1337, ssl=True)

r.recvuntil(
    b"2 - Read Hash record\n"
)  # wait until we receive this text... which is when we need to response

for i in range(10):
    r.sendline(b"2")  # and send the command
    r.recvuntil(b"Idx: ")
    idx = (1464 // 8) + i
    r.sendline(str(idx).encode())  # convert `idx` to string, and send it
    hash_hex = r.recvline().split(b":")[1].strip()
    hash_bytes = bytes.fromhex(hash_hex.decode())
    print(hash_bytes)
r.interactive()
