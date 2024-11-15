

# This file was *autogenerated* from the file problem.mod.sage
from sage.all_cmdline import *   # import sage library

_sage_const_65537 = Integer(65537); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_71415146914196662946266805639224515745292845736145778437699059682221311130458 = Integer(71415146914196662946266805639224515745292845736145778437699059682221311130458); _sage_const_62701913347890051538907814870965077916111721435130899071333272292377551546304 = Integer(62701913347890051538907814870965077916111721435130899071333272292377551546304); _sage_const_60374783698776725786512193196748274323404201992828981498782975421278885827246 = Integer(60374783698776725786512193196748274323404201992828981498782975421278885827246); _sage_const_60410367194208847852312272987063897634106232443697621355781061985831882747944 = Integer(60410367194208847852312272987063897634106232443697621355781061985831882747944); _sage_const_57454549555647442495706111545554537469908616677114191664810647665039190180615 = Integer(57454549555647442495706111545554537469908616677114191664810647665039190180615); _sage_const_8463288093684346104394651092611097313600237307653573145032139257020916133199 = Integer(8463288093684346104394651092611097313600237307653573145032139257020916133199); _sage_const_38959331790836590587805534615513493167925052251948090437650728000899924590900 = Integer(38959331790836590587805534615513493167925052251948090437650728000899924590900); _sage_const_62208987621778633113508589266272290155044608391260407785963749700479202930623 = Integer(62208987621778633113508589266272290155044608391260407785963749700479202930623); _sage_const_0 = Integer(0); _sage_const_3 = Integer(3)
import os
from hashlib import sha256
from secrets import randbelow

from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes


FLAG = os.getenvb(b"FLAG", b"FAKEFLAG{THIS_IS_FAKE}")

# p = 0xC20C8EDB31BFFA707DC377C2A22BE4492D1F8399FFFD388051EC5E4B68B4598B
p = _sage_const_65537 
order = p**_sage_const_2  - _sage_const_1 
Q = QuaternionAlgebra(Zmod(p), -_sage_const_1 , -_sage_const_1 )
i, j, k = Q.gens()

pub_A = (
    _sage_const_71415146914196662946266805639224515745292845736145778437699059682221311130458 
    + _sage_const_62701913347890051538907814870965077916111721435130899071333272292377551546304  * i
    + _sage_const_60374783698776725786512193196748274323404201992828981498782975421278885827246  * j
    + _sage_const_60410367194208847852312272987063897634106232443697621355781061985831882747944  * k
)

pub_B = (
    _sage_const_57454549555647442495706111545554537469908616677114191664810647665039190180615 
    + _sage_const_8463288093684346104394651092611097313600237307653573145032139257020916133199  * i
    + _sage_const_38959331790836590587805534615513493167925052251948090437650728000899924590900  * j
    + _sage_const_62208987621778633113508589266272290155044608391260407785963749700479202930623  * k
)


def quaternion2matrix(q):
    a, b, c, d = q
    return matrix(
        [
            [a, b, c, d],
            [-b, a, -d, c],
            [-c, d, a, -b],
            [-d, -c, b, a],
        ]
    )


pub_A = quaternion2matrix(pub_A)
pub_B = quaternion2matrix(pub_B)

print(pub_A**order)
print(pub_B**order)

print(pub_A)
print(pub_A ** (p - _sage_const_1 ))
print(pub_A ** (p + _sage_const_1 ))


def hash_Q(x):
    return sha256(
        long_to_bytes(int(x[_sage_const_0 ]))
        + long_to_bytes(int(x[_sage_const_1 ]))
        + long_to_bytes(int(x[_sage_const_2 ]))
        + long_to_bytes(int(x[_sage_const_3 ]))
    ).digest()


if __name__ == "__main__":
    # Alice sends share_A to Bob
    priv_A = randbelow(order)
    print(f"{pub_A = }")
    A = pub_A**priv_A
    print(f"{A = }")
    print(f"{A**-_sage_const_1  = }")
    share_A = A**-_sage_const_1  * pub_B * A
    # assert share_A == pub_B
    print(f"{share_A = }")
    # Bob sends share_B to Alice
    priv_B = randbelow(order)
    B = pub_B**priv_B
    print(f"{B = }")
    print(f"{B**-_sage_const_1  = }")
    share_B = B**-_sage_const_1  * pub_A * B
    print(f"{share_B = }")
    # Alice computes the shared key
    Ka = A**-_sage_const_1  * share_B**priv_A
    # Bob computes the shared key
    Kb = share_A**-priv_B * B
    assert Ka == Kb

    assert Ka == pub_A**-priv_A * pub_B**-priv_B * pub_A**priv_A * pub_B**priv_B
    assert Kb == pub_A**-priv_A * pub_B**-priv_B * pub_A**priv_A * pub_B**priv_B

    # Encrypt FLAG with the shared key
    # key = hash_Q(Ka)
    # cipher = AES.new(key, mode=AES.MODE_CTR)
    # nonce = cipher.nonce.hex()
    # enc = cipher.encrypt(FLAG).hex()
    # print(f"{nonce = }")
    # print(f"{enc = }")

