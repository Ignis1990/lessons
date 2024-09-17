# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(number_1, number_2, number_3):
    num_list = [number_1, number_2, number_3]
    num_list.sort(reverse=True)
    return num_list[0] + num_list[1]


a = my_func(7, 5, 8)
print(a)