# # Task № 1. Дана строка 'AaBbCcDd'. Используя срезы с шагом получите две строки: только с заглавными и только со строчными буквами.
# # Выведите их на экран.
#
# letters = 'AaBbCcDd'
# cap_letters = letters[::2]
# low_letters = letters[1::2]
# print(f'{cap_letters}, {low_letters}')

# # Task № 2. Дан список натуральных чисел [13, 5, 5, 8, 16, 4]. Удалите из него первое четное число, имеющее нечетный индекс.
# # Выведите измененный список на экран.
#
# num_list = [13, 5, 5, 8, 16, 4]
# for i in range(1, len(num_list), 2):
#     if num_list[i] % 2 == 0:
#         num_list.pop(i)
#         break
# print(num_list)
#
# или
#
# num_list = [13, 5, 5, 8, 16, 4]
# for i in range(0, len(num_list)):
#     if num_list[i] % 2 == 0 and i % 2 != 0:
#         num_list.pop(i)
#         break
# print(num_list)

# # Task № 3. Рассчитать стоимость покупки с учетом скидки в 35%, которая предоставляется покупателю, если сумма покупки
# # превышает 20 у.е. Сумму покупки ввести с клавиатуры, а результаты округлить до сотых (копейки, центы и т.д.). Вывести на
# # экран итоговую стоимость и размер предоставленной скидки.
#
# original_price = int(input(f'Введите сумму покупки: '))
# sale = 0.35
# if original_price > 20:
#     sale_price = original_price - (original_price * sale)
#     sale_value = original_price * sale
# print(f'Сумма покупки составила {sale_price:.2f}, размер скидки - {sale_value:.2f}')