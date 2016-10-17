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


def main():
    number = 255.6541
    print('Dec: ', number)
    binar = dec_to_bin(number)
    print('Bin: ', binar)
    number = bin_to_hex(binar)
    print('Hex: ', number)
    number = bin_to_oct(binar)
    print('Oct: ', number)

    rows, columns = os.popen('stty size', 'r').read().split()
    double_stripe = int(columns) * '='
    print(double_stripe)

    number = 30
    print('Dec: ', number)
    binar = dec_to_bin(number)
    print('Bin: ', binar)
    number = bin_to_hex(binar)
    print('Hex: ', number)
    number = bin_to_oct(binar)
    print('Oct: ', number)


if __name__ == "__main__":
    main()
