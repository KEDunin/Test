lst_main = list()

try:
    num_list = (input("Вводите числа через пробел: ")).split()
    lst_main = list(map(int, num_list))
    print(lst_main)

except ValueError:
    print(-1)
    exit(1)

# Использование списковых выражений
print("Чётные числа:", [i * 1 for i in lst_main if (i % 2 == 0)])
print("Нечётные числа:", [i * 1 for i in lst_main if (i % 2 == 1)])
print("Отрицательные числа:", [i * 1 for i in lst_main if i < 0])

# Использование функций высших порядков
lst_even_num = filter(lambda x: x % 2 == 0, lst_main)
lst_even_num = map(lambda x: x * 1, lst_even_num)
print("Чётные числа:", list(lst_even_num))

lst_uneven_num = filter(lambda x: x % 2 == 1, lst_main)
lst_uneven_num = map(lambda x: x * 1, lst_uneven_num)
print("Нечётные числа:", list(lst_uneven_num))

lst_negative_num = filter(lambda x: x < 0, lst_main)
lst_negative_num = map(lambda x: x * 1, lst_negative_num)
print("Отрицательные числа:", list(lst_negative_num))
