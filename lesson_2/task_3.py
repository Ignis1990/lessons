user_input = input(f'Введите целое положительное число: ')

max_number = 0
for i in user_input:
    if int(i) > max_number:
        max_number = int(i)
print(max_number)
