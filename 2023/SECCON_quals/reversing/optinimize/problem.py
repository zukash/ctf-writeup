def P(arg_j):
    i = 3
    j = 0
    k = 2
    if arg_j == 0:
        return i

    if arg_j == 1:
        return j

    if arg_j == 2:
        return k

    o = 2
    if o < arg_j:  # maybe always true
        arg_j_copy = arg_j
        while True:
            if not (2 < arg_j_copy):
                return k

            ij_result = i + j
            i = j
            j = k
            k = ij_result
            arg_j_copy = arg_j_copy - 1


def Q(input):
    i = 0
    j = 0

    while True:
        if not (i < input):
            return j
        j = j + 1

        p_res = P(j)
        p_res_mod = p_res % j

        if p_res_mod == 0:
            i = i + 1


inputs = [
    0x0000004A,
    0x00000055,
    0x0000006F,
    0x00000079,
    0x00000080,
    0x00000095,
    0x000000AE,
    0x000000BF,
    0x000000C7,
    0x000000D5,
    0x00000306,
    0x00001AC8,
    0x000024BA,
    0x00003D00,
    0x00004301,
    0x00005626,
    0x00006AD9,
    0x00007103,
    0x0000901B,
    0x00009E03,
    0x001E5FB6,
    0x0026F764,
    0x0030BD9E,
    0x00407678,
    0x005B173B,
    0x006FE3B1,
    0x0078EF25,
    0x00858E5F,
    0x0098C639,
    0x00AD6AF6,
    0x01080096,
    0x018E08CD,
    0x01BB6107,
    0x01F50FF1,
    0x025C6327,
    0x02A971B6,
    0x02D68493,
    0x0362F0C0,
    0x03788EAD,
    0x03CAA8ED,
]


xor_target = [
    0x3C,
    0xF4,
    0x1A,
    0xD0,
    0x8A,
    0x17,
    0x7C,
    0x4C,
    0xDF,
    0x21,
    0xDF,
    0xB0,
    0x12,
    0xB8,
    0x4E,
    0xFA,
    0xD9,
    0x2D,
    0x66,
    0xFA,
    0xD4,
    0x95,
    0xF0,
    0x66,
    0x6D,
    0xCE,
    0x69,
    0x00,
    0x7D,
    0x95,
    0xEA,
    0xD9,
    0x0A,
    0xEB,
    0x27,
    0x63,
    0x75,
    0x11,
    0x37,
    0xD4,
]

QQ = Primes()

def main():
    for i, input in enumerate(inputs):
        # print(Q(input) % 255)
        print(chr((Q(input) % 255) ^ xor_target[i]))
    print()


main()
