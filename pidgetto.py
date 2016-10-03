import os


# Функция выбора системы счисления
def get_num_sys(msg):
    while True:
        num_sys = print(msg)
        num_sys = input('>>>')
        num_sys = num_sys.upper()
        if num_sys == 'BIN':
            return 2
        elif num_sys == 'OCT':
            return 8
        elif num_sys == 'DEC':
            return 10
        elif num_sys == 'HEX':
            return 16


# Функция перевода из двоичной системы
def convert_num_sys(value, f_num_sys, t_num_sys):
    value = int(value, f_num_sys)
    if t_num_sys == 2:
        return bin(value)
    elif t_num_sys == 8:
        return oct(value)
    elif t_num_sys == 10:
        return value
    elif t_num_sys == 16:
        return hex(value)


def main():
    msg = 'Выберите начальную систему счисления: BIN, OCT, DEC, HEX'
    f_num_sys = get_num_sys(msg)  # Получаем исходную систему исчисления
    print('Перевод из {}ичной системы'.format(f_num_sys))
    print()
    msg = 'Выберите систему счисления для результата: BIN, OCT, DEC, HEX'
    # Получаем систему счисления, в которую необходимо перевести
    t_num_sys = get_num_sys(msg)
    print()
    print('Введите значение:')
    value = input('>>>')  # Получаем исходное число
    print()
    try:
        rows, columns = os.popen('stty size', 'r').read().split()
        res = convert_num_sys(value, f_num_sys, t_num_sys)
        msg = str(int(columns) * '-')
        print(msg)
        print('Результат вычислений:')
        print(res)
        print()
    except ValueError:
        c = int(columns)
        msg = ' Неверное число. Проверьте систему счисления '.center(c, '!')
        print(msg)
    except TypeError:
        print('!!! Это не число. Выходим. !!!'.center(int(columns), ' '))
    print(str(int(columns) * '='))
    print('Pidgey'.center(int(columns), ' '))
    print(str(int(columns) * '='))
    main()

rows, columns = os.popen('stty size', 'r').read().split()
print(str(int(columns) * '='))
print('Pidgey v2.4'.center(int(columns), ' '))
print(str(int(columns) * '='))


main()
