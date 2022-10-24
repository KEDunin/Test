num_list = (input("Вводите числа через пробел: ")).split()
lst_main = list(map(int, num_list))
print(lst_main)

# Использование списковых выыражений
print([i * 1 for i in lst_main if (i % 2 == 0)])
print([i * 1 for i in lst_main if (i % 2 == 1)])
print([i * 1 for i in lst_main if i < 0])

# Использование функций высших порядков
lst_even_num = filter(lambda x: x % 2 == 0, lst_main)
lst_even_num = map(lambda x: x * 1, lst_even_num)
print(list(lst_even_num))

lst_uneven_num = filter(lambda x: x % 2 == 1, lst_main)
lst_uneven_num = map(lambda x: x * 1, lst_uneven_num)
print(list(lst_uneven_num))

lst_negative_num = filter(lambda x: x < 0, lst_main)
lst_negative_num = map(lambda x: x * 1, lst_negative_num)
print(list(lst_negative_num))
