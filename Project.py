# Создание пустых списков для хранения в них соответствующих выполненных операций
lst1 = list()
lst2 = list()
lst3 = list()
lst4 = list()

# Объявление переменных с пустым значением
a = None
operator = None
b = None
result = None

while True:  # Запуск бесконечного цикла
    print("Введите переменную а:")
    a = float(input("а = "))
    print("Введите оператор (сложения, вычитания, умножения или деления):")
    operator = input("оператор:")
    if (operator == "+") or (operator == "-") or (operator == "*") or (operator == "/"):
        print("Введите переменную b: ")
        b = float(input("b = "))
        if (operator == "/") and (b == 0):  # Проверка деления на ноль
            try:
                print("Деление на ноль невозможно!Введите переменную b ещё раз:")
                b = float(input("b = "))
            except ZeroDivisionError:
                pass
    else:
        print("Неверный оператор!")

    # Выполнение операции, соответствующей выбранному оператору (действию над числами)
    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        result = a / b
        result = result.__round__(3)  # Округление числа после выполнения деления в целях обеспечения краткости записи

    # Запись результата в переменную типа str для последующего вывода на экран и добавления ее в один из списков
    strresult = f"{a} {operator} {b} = {result}"
    print("Результат:", strresult)

    # Ведение истории выполненных операций
    if operator == "+":
        lst1.append(strresult)
    elif operator == "-":
        lst2.append(strresult)
    elif operator == "*":
        lst3.append(strresult)
    elif operator == "/":
        lst4.append(strresult)

    print("-" * 35)
    print("История операций:")
    print("Сложение:", lst1)
    print("Вычитание:", lst2)
    print("Умножение:", lst3)
    print("Деление:", lst4)
    print("-" * 35)
