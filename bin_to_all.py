# -*- coding: utf-8 -*-

def dec_to_bin(num):
    int_part = int(num)
    float_part = num - int(num)

    bin_int_part = 0
    bin_float_part = 0
    i = 1
    j = 0.1

    while int_part > 0:
        bin_int_part = bin_int_part + int_part % 2 * i
        i = i * 10
        int_part = int(int_part / 2)

    while j > 0.00000001:
        tmp = float_part * 2
        bin_float_part = bin_float_part + (int(tmp)) * j
        float_part = tmp - int(tmp)
        j = j / 10

    bin_full = bin_int_part + bin_float_part
    print('Bin Full: ''{:.8f}'.format(bin_full))

    return bin_int_part, bin_float_part


def bin_to_hex(hex_int, hex_float):
    dic = {'0000': '0', '1000': '8',
           '0001': '1', '1001': '9',
           '0010': '2', '1010': 'A',
           '0011': '3', '1011': 'B',
           '0100': '4', '1100': 'C',
           '0101': '5', '1101': 'D',
           '0110': '6', '1110': 'E',
           '0111': '7', '1111': 'F'}

    print ('Int Part: ', hex_int)
    print ('Float Part: ', hex_float)
    hex_int = str(hex_int)
    while (len(hex_int) % 4 != 0):
        hex_int = '0' + hex_int

    hex_full = ''
    cut1 = 0
    cut2 = 4
    while (len(hex_int) >= cut2):
        temp = hex_int[cut1:cut2]
        for key in dic.keys():
            temp = temp.replace(key, dic[key])
        cut1 += 4
        cut2 += 4
        hex_full += temp

    hex_float = str(hex_float)[2:]
    while (len(hex_float) % 4 != 0):
        hex_float = hex_float + '0'

    hex_full += '.'

    cut1 = 0
    cut2 = 4
    while (len(hex_float) >= cut2):
        temp = hex_float[cut1:cut2]
        for key in dic.keys():
            temp = temp.replace(key, dic[key])
        cut1 += 4
        cut2 += 4
        hex_full += temp

    return hex_full


def bin_to_oct(oct_int, oct_float):
    dic = {'000': '0', '100': '4',
           '001': '1', '101': '5',
           '010': '2', '110': '6',
           '011': '3', '111': '7'}

    oct_int = str(oct_int)
    while (len(oct_int) % 3 != 0):
        oct_int = '0' + oct_int

    oct_full = ''
    cut1 = 0
    cut2 = 3
    while (len(oct_int) >= cut2):
        temp = oct_int[cut1:cut2]
        for key in dic.keys():
            temp = temp.replace(key, dic[key])
        cut1 += 3
        cut2 += 3
        oct_full += temp

    oct_float = str(oct_float)[2:]
    while (len(oct_float) % 3 != 0):
        oct_float = oct_float + '0'
    oct_full += '.'

    cut1 = 0
    cut2 = 3
    while (cut2 <= len(oct_float)):
        temp = oct_float[cut1:cut2]
        for key in dic.keys():
            temp = temp.replace(key, dic[key])
        cut1 += 3
        cut2 += 3
        oct_full += temp

    print('Oct Full: ', oct_full)

    return oct_full


hex_int, hex_float = dec_to_bin(255.6541)
bin_to_hex(hex_int, hex_float)
bin_to_oct(hex_int, hex_float)
print('===========================')
hex_int, hex_float = dec_to_bin(30)
bin_to_hex(hex_int, hex_float)
bin_to_oct(hex_int, hex_float)
