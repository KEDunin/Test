def work_with_console(func):
    def wrapper(*args, **kwargs):
        a = float(input("Введите переменную a: "))
        b = float(input("Введите переменную b: "))
        result = func(a, b).__round__(3)
        print(f"Результат {result}")
        print("")
        return func(*args, **kwargs)
    return wrapper


@work_with_console
def calculation(a, b):
    return (a + b) / b * a


while True:
    calculation()
