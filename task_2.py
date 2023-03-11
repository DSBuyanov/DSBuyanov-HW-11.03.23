# Задача 32: Определить индексы элементов массива(списка),
# значения которых принадлежат заданному диапазону(т.е. не меньше заданного минимума и не больше заданного максимума)

def find_indexes(lst, min_val, max_val):
    indexes = []
    for i in range(len(lst)):
        if min_val <= lst[i] <= max_val:
            indexes.append(i)
    return indexes

my_list = [0, 2, 5, -7, 110, 16]
min_val = 3
max_val = 15
result = find_indexes(my_list, min_val, max_val)
print(result)