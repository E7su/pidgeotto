# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def dec_to_bin(num):
    num = str(num)
    num = num.split('.')
    bin_int = bin(int(num[0]))
    bin_int = str(bin_int)[2:]
    bin_float = 0

    try:
        float_part = float('0.' + num[1])
        i = 1
        j = 0.1

        while j > 0.0000000000000000000001:  # todo
            tmp = float_part * 2
            bin_float = bin_float + (int(tmp)) * j
            float_part = tmp - int(tmp)
            j = j / 10

    except IndexError:
        pass

    bin_full = str(int(bin_int) + bin_float)

    return bin_full


def bin_to_hex(num):
    dic = {'0000': '0', '1000': '8',
           '0001': '1', '1001': '9',
           '0010': '2', '1010': 'A',
           '0011': '3', '1011': 'B',
           '0100': '4', '1100': 'C',
           '0101': '5', '1101': 'D',
           '0110': '6', '1110': 'E',
           '0111': '7', '1111': 'F'}

    num = str(num)
    num = num.split('.')
    hex_int = hex(int(num[0], 2))
    hex_int = str(hex_int)[2:]
    hex_full = hex_int

    try:
        hex_float = str(num[1])
        hex_full += '.'

        while (len(hex_float) % 4 != 0):
            hex_float += '0'

        cut1 = 0
        cut2 = 4
        while (len(hex_float) >= cut2):
            temp = hex_float[cut1:cut2]
            for key in dic.keys():
                temp = temp.replace(key, dic[key])
            cut1 += 4
            cut2 += 4
            hex_full += temp

    except IndexError:
        pass

    return hex_full.upper()


def hex_to_bin(num):
    dic = {'0000': '0', '1000': '8',
           '0001': '1', '1001': '9',
           '0010': '2', '1010': 'A',
           '0011': '3', '1011': 'B',
           '0100': '4', '1100': 'C',
           '0101': '5', '1101': 'D',
           '0110': '6', '1110': 'E',
           '0111': '7', '1111': 'F'}

    num = str(num)
    num = num.split('.')
    bin_int = bin(int(num[0], 16))
    bin_int = str(bin_int)[2:]
    bin_full = bin_int

    try:
        bin_float = str(num[1])
        bin_full += '.'

        while (len(bin_float) % 4 != 0):
            bin_float += '0'

        cut1 = 0
        cut2 = 4
        while (len(bin_float) >= cut2):
            temp = bin_float[cut1:cut2]
            for key in dic.keys():
                temp = temp.replace(dic[key], key)
            cut1 += 4
            cut2 += 4
            bin_full += temp

    except IndexError:
        pass

    return bin_full


def bin_to_oct(num):
    dic = {'000': '0', '100': '4',
           '001': '1', '101': '5',
           '010': '2', '110': '6',
           '011': '3', '111': '7'}

    num = str(num)
    num = num.split('.')
    oct_int = oct(int(num[0], 2))
    oct_full = str(oct_int)[2:]

    try:
        oct_float = num[1]
        oct_full += '.'

        while (len(oct_float) % 3 != 0):
            oct_float += '0'

        cut1 = 0
        cut2 = 3
        while (cut2 <= len(oct_float)):
            temp = oct_float[cut1:cut2]
            for key in dic.keys():
                temp = temp.replace(key, dic[key])
            cut1 += 3
            cut2 += 3
            oct_full += temp

    except IndexError:
        pass

    return oct_full


def oct_to_bin(num):
    dic = {'000': '0', '100': '4',
           '001': '1', '101': '5',
           '010': '2', '110': '6',
           '011': '3', '111': '7'}

    num = str(num)
    num = num.split('.')
    bin_int = bin(int(num[0], 8))
    bin_full = str(bin_int)[2:]

    try:
        bin_float = num[1]
        bin_full += '.'

        while (len(bin_float) % 3 != 0):
            bin_float += '0'

        cut1 = 0
        cut2 = 3
        while (cut2 <= len(bin_float)):
            temp = bin_float[cut1:cut2]
            for key in dic.keys():
                temp = temp.replace(dic[key], key)
            cut1 += 3
            cut2 += 3
            bin_full += temp

    except IndexError:
        pass

    return bin_full


def main():
    decim = 255.6541
    print('VALUE: ', decim)

    binar = dec_to_bin(decim)
    print('DEC -> BIN: ', binar)

    octal = bin_to_oct(binar)
    print('BIN -> OCT: ', octal)

    hexim = bin_to_hex(binar)
    print('BIN -> HEX: ', hexim)

    binar = hex_to_bin(hexim)
    print('HEX -> BIN: ', binar)

    binar = oct_to_bin(octal)
    print('OCT -> BIN: ', binar)

    # rows, columns = os.popen('stty size', 'r').read().split()  # todo for terminal
    columns = 70
    double_stripe = int(columns) * '='
    print(double_stripe)


if __name__ == "__main__":
    main()
