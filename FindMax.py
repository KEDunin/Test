numbers = input("Введите числа через пробел:")
list_of_numbers = numbers.split(" ")
print(list_of_numbers)


def find_max(set_numbers):
    control_number = int(set_numbers[0])
    for i in range(len(set_numbers) - 1):
        if int(set_numbers[i + 1]) > control_number:
            control_number = int(set_numbers[i + 1])
    return control_number


result = find_max(list_of_numbers)
print(f"Максимальное число: {result}")
print("-" * 40)


# Второй вариант с использованием готового списка чисел

list_of_numbers2 = [12, 34, 0, 1, 0, 103, 76, 31, 2, 84]
print("Готовый набор чисел:", list_of_numbers2)
result = find_max(list_of_numbers2)
print(f"Максимальное число: {result}")
