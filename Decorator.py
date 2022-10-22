def work_with_console(func):
    def wrapper(*args, **kwargs):
        first = input("Введите число а:")
        second = input("Введите число b:")
        first, second = args
        answer = calculation(first, second)
        print(answer)
        return func(*args, **kwargs)
    return wrapper


@work_with_console
def calculation(a, b):
    return (a + b) / b * a