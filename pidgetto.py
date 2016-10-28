# !/usr/lib/python3.4
# -*- coding: utf-8 -*-

from bin_to_all import *
from all_to_dec import *


def convertation(num, from_base, to_base):
    DOCUMENTATION = """
    module: pidgeotto
    version_added: "1.0"
    description:
      - Convert all systems
    description:
      - Create VM.
    options:
      num:
        description:
          - The number for convertation.
      from_base:
        description:
          - The positional numeral system of the number
            which we will translate.
      to_base:
        description:
          - The positional numeral system for result.
    author: "Polina Azarova (@e7su)"
    note:
      2 ->  2 print num  ###
      2 ->  8 bin_to_oct
      2 -> 10 all_to_dec  #
      2 -> 16 bin_to_hex

      8 ->  2 oct_to_dec, dec_to_bin
      8 ->  8 print num  ###
      8 -> 10 all_to_dec  #
      8 -> 16 oct_to_dec, dec_to_bin, bin_to_hex

      10 ->  2 dec_to_bin
      10 ->  8 dec_to_bin, bin_to_oct
      10 -> 10 print num  ###
      10 -> 16 dec_to_bin, bin_to_hex

      16 ->  2 all_to_dec, dec_to_bin
      16 ->  8 all_to_dec,dec_to_bin, bin_to_oct
      16 -> 10 all_to_dec  #
      16 -> 16 print num  ###
    """

    if to_base == from_base:
        return num
    else:

        if to_base == 10:
            return all_to_dec(num, from_base)
        else:

            if from_base == 2:
                if to_base == 8:
                    return bin_to_oct(num)
                else:
                    return bin_to_hex(num)

            if from_base == 8:
                if to_base == 2:
                    return dec_to_bin(oct_to_dec(num))
                else:
                    return bin_to_hex(dec_to_bin(oct_to_dec(num)))

            if from_base == 10:
                if to_base == 2:
                    return dec_to_bin(num)
                if to_base == 8:
                    return bin_to_oct(dec_to_bin(num))
                else:
                    return bin_to_hex(dec_to_bin(num))

            if from_base == 16:
                if to_base == 2:
                    return dec_to_bin(all_to_dec(num, 16))
                if to_base == 8:
                    return bin_to_oct(dec_to_bin(all_to_dec(num, 16)))


def main():
    a = (12, 10.0, 'FF.A7', 202.01)
    fb = (10, 10, 16, 2)
    tb = (2, 8, 2, 2)
    for i in range(len(a)):
        print('Num:       ', a[i])
        print('From Base: ', fb[i])
        print('To Base:   ', tb[i])
        print('Res:       ', convertation(a[i], fb[i], tb[i]))
        print()


if __name__ == "__main__":
    main()
