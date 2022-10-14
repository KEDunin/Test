lst1 = list()
lst2 = list()
lst3 = list()
lst4 = list()
a = None
while True:
   
        try:
            print("Введите переменную а:")
            a = float(input("а = "))
        except ValueError:
            print("Некорректный формат числа")
    print("Введите оператор (сложения, вычитания, умножения или деления):")
    operand = input("оператор:")
    if (operand == "+") or (operand == "-") or (operand == "*") or (operand == "/"):
        print("Введите переменную b: ")
        b = float(input("b = "))
    else:
        print("Неверный оператор!")

    if operand == "+":
        result = a + b
    elif operand == "-":
        result = a - b
    elif operand == "*":
        result = a * b
    elif operand == "/":
        result = a / b
        result = result.__round__(3)


    strresult = f"{a} {operand} {b} = {result}"
    print("Результат:", strresult)

    if operand == "+":
        lst1.append(strresult)
    elif operand == "-":
        lst2.append(strresult)
    elif operand == "*":
        lst3.append(strresult)
    elif operand == "/":
        lst4.append(strresult)

    print("-" * 35)
    print("История операций:")
    print("Сложение:", lst1)
    print("Вычитание:", lst2)
    print("Умножение:", lst3)
    print("Деление:", lst4)
    print("-" * 35)



