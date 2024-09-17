lst = [1, 2, 3, 4, 5, 6]

for i in range(0, len(lst), 2):
    element = lst.pop(i)
    lst.insert(i + 1, element)
print(lst)