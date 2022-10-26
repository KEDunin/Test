def work_with_console(func):
    def wrapper(*args, **kwargs):
        a = float(input("Введите переменную a: "))  # Ввод функции
        b = float(input("Введите переменную b: "))  # Ввод функции
        result = func(a, b, *args, **kwargs)  # Работа с любыми параметрами функции
        print(f"Результат {result}")  # Вывод функции
        return result
    return wrapper


@work_with_console
def calculation(a, b, fir_word, sec_word, th_word):
    return ((a + b) / b * a), fir_word, sec_word, th_word


calculation("Lucky", "experiment", "))")
