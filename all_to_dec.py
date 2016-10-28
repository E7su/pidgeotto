# -*- coding: utf-8 -*-


def all_to_dec(num, base):

    dec_int = 0
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
            dec_int += 10 * base ** i
            cut1 += 1
            cut2 += 1
            i -= 1
        elif temp[cut1:cut2] == 'B':
            dec_int += 11 * base ** i
            cut1 += 1
            cut2 += 1
            i -= 1
        elif temp[cut1:cut2] == 'C':
            dec_int += 12 * base ** i
            cut1 += 1
            cut2 += 1
            i -= 1
        elif temp[cut1:cut2] == 'D':
            dec_int += 13 * base ** i
            cut1 += 1
            cut2 += 1
            i -= 1
        elif temp[cut1:cut2] == 'E':
            dec_int += 14 * base ** i
            cut1 += 1
            cut2 += 1
            i -= 1
        elif temp[cut1:cut2] == 'F':
            dec_int += 15 * base ** i
            cut1 += 1
            cut2 += 1
            i -= 1

        else:
            dec_int += int(temp[cut1:cut2]) * base ** i
            cut1 += 1
            cut2 += 1
            i -= 1

    return float(dec_int)


def main():
    a = (101.01, 10.0, 'FF.A7', 202.01)
    fb = (2, 8, 16, 2)
    for i in range(len(a)):
        print('Num:       ', a[i])
        print('From Base: ', fb[i])
        print('Res:       ', all_to_dec(a[i], fb[i]))
        print()

if __name__ == "__main__":
    main()
