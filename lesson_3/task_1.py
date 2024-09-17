# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Число запрашивается у
# пользователя, предусмотреть деление на ноль


def divide_2_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Нельзя'


def main():
    inp_a = int(input('Введите первое число: '))
    inp_b = int(input('Введите второе число: '))
    result = divide_2_numbers(inp_a, inp_b)
    print(result)


main()