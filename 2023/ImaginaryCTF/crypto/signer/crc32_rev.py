# https://qiita.com/taiyaki8926/items/94b8f12973d477749d10

import binascii
import codecs


def crc32_rewind(data, crc):
    crc = 0xFFFFFFFF ^ crc
    for c in data[::-1]:
        for i in range(8):
            if crc <= 0x7FFFFFFF:
                crc = crc << 1
            else:
                crc = ((crc ^ 0xEDB88320) << 1) + 1
        crc = crc ^ c
    return 0xFFFFFFFF ^ crc


c2 = 4148080273
crc32_rewind(b"hello_world", c2)
# -> 0


def crc32_rev(genuine, fake, crc_init):
    # step 1.
    genuine_crc = binascii.crc32(genuine, crc_init)
    fake_crc = binascii.crc32(fake, crc_init)
    # 16進数で8桁未満になった場合にゼロでパディング
    crc_pad = 8 - len("%x" % fake_crc)
    byte = codecs.decode("0" * crc_pad + ("%x" % fake_crc), "hex_codec")[::-1]
    # step 2.
    ans_rev = crc32_rewind(byte, genuine_crc)
    # step 3.
    ans_pad = 8 - len("%x" % ans_rev)
    ans = codecs.decode(("0" * ans_pad + "%x" % ans_rev), "hex_codec")[::-1]
    print(
        "binascii.crc32({}, {}) == binascii.crc32({}, {})".format(
            genuine, crc_init, (fake + ans), crc_init
        )
    )
    return ans


def crc32_rev_mod(genuine_crc, fake, crc_init):
    # step 1.
    fake_crc = binascii.crc32(fake, crc_init)
    # 16進数で8桁未満になった場合にゼロでパディング
    crc_pad = 8 - len("%x" % fake_crc)
    byte = codecs.decode("0" * crc_pad + ("%x" % fake_crc), "hex_codec")[::-1]
    # step 2.
    ans_rev = crc32_rewind(byte, genuine_crc)
    # step 3.
    ans_pad = 8 - len("%x" % ans_rev)
    ans = codecs.decode(("0" * ans_pad + "%x" % ans_rev), "hex_codec")[::-1]
    print(
        "binascii.crc32({}, {}) == binascii.crc32({}, {})".format(
            genuine_crc, crc_init, (fake + ans), crc_init
        )
    )
    return ans


crc32_rev(b"hello_world", b"123", 0)
# -> binascii.crc32(b'hello_world', 0) == binascii.crc32(b'123F\xa9\xd3\x0c', 0)
# -> b'F\xa9\xd3\x0c'


crc32_rev(b"give me the flag!!!", b"123", 0)


crc32_rev_mod(binascii.crc32(b"give me the flag!!!"), b"123", 0)
crc32_rev_mod(3, b"123", 0)
crc32_rev_mod(7 * 12517 * 13477, b"123", 0)
