import phonenumbers
import pandas as pd

file_path = "./phonebook.csv"
phonebook = pd.read_csv(file_path)

def is_printable(s):
    for c in s:
        if c < 0x20 or c > 0x7e:
            return False
    return True

for i, phone_number in enumerate(phonebook["PHONE_NUMBER"]):
    try:
        flag = bytes.fromhex(phone_number)
        assert is_printable(flag)
        # aからfが含まれている
        assert sum([x in phone_number for x in 'abcdef']) >= 1
        print(flag.decode(), end='')
    except:
        continue
    # try:
    #     pn = phonenumbers.parse(phone_number, "JP")
    # except:
    #     print(phonebook.iloc[i])

