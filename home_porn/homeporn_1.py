# Дан список, состоящий из цифр: 9, 7, 6, 6, 5, 3, 1.
# Необходимо реализовать функцию добавления пользователем элементов списка (цифр) таким образом, чтобы новый элемент
# списка, во-первых, сортировался, как и список, в убывающем порядке, во-вторых - при добавлении значения, которое уже есть
# в списке оно добавлялось ПОСЛЕ уже имеющегося значения.

this_list = [9, 7, 6, 6, 5, 3, 1]
user_input = int(input(f'Введите цифру: '))

# for i in range(len(this_list)):
#     if user_input > this_list[i]:
#         this_list.insert(i ,user_input)

i = 0
while i < len(this_list) and user_input < this_list[i]:
    i += 1
this_list.insert(i, user_input)
print(this_list)