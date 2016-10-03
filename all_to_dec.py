# -*- coding: utf-8 -*-

def to_dec(num, base):

    print(num)

    dec_int_part = 0
    i = 0
    cut1 = 0
    cut2 = 1

    temp = str(num).upper()

    while temp[cut1:cut2] != '.':
        cut1 += 1
        cut2 += 1
        i += 1

    cut1 = 0
    cut2 = 1
    i -= 1

    while len(str(num)) >= cut2:
        if temp[cut1:cut2] == '.':
            cut1 += 1
            cut2 += 1
        elif temp[cut1:cut2] == 'A':
            dec_int_part += 10 * base ** i
            cut1 += 1
            cut2 += 1
            i -= 1
        elif temp[cut1:cut2] == 'B':
            dec_int_part += 11 * base ** i
            cut1 += 1
            cut2 += 1
            i -= 1
        elif temp[cut1:cut2] == 'C':
            dec_int_part += 12 * base ** i
            cut1 += 1
            cut2 += 1
            i -= 1
        elif temp[cut1:cut2] == 'D':
            dec_int_part += 13 * base ** i
            cut1 += 1
            cut2 += 1
            i -= 1
        elif temp[cut1:cut2] == 'E':
            dec_int_part += 14 * base ** i
            cut1 += 1
            cut2 += 1
            i -= 1
        elif temp[cut1:cut2] == 'F':
            dec_int_part += 15 * base ** i
            cut1 += 1
            cut2 += 1
            i -= 1

        else:
            dec_int_part += int(temp[cut1:cut2]) * base ** i
            cut1 += 1
            cut2 += 1
            i -= 1

    print(dec_int_part)

to_dec(101.01, 2)
print()
to_dec(10.0, 8)
print()
to_dec('FF.A7', 16)
print()
to_dec(202.01, 2)
print()
