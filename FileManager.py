import os
from pathlib import Path

t_dir = os.getcwd()

while True:  # Вход в бесконечный цикл
    value = str(input("Введите название команды, которую необходимо выполнить: "))
    a = value.split(" ")  # Создание списка, содержащего вводимые в консоль данные
    if a[0] == "pwd":
        print("Путь текущей папки:", t_dir)
    elif a[0] == "cd":
        try:
            t_dir = Path(t_dir) / a[1]
            os.chdir(t_dir)
            print("Переход к вложенной папке... ", t_dir)
        except FileNotFoundError:  # Обработка исключений
            print("Папка с таким именем отсутствует в данной директории")
    elif a[0] == "touch":
        with open(a[1], "w") as file:
            file.write(" ")  # Запись пустого файла
    elif a[0] == "cat":
        try:
            with open(a[1], "r") as file:
                for line in file:  # Построчное чтение кода
                    print(line.strip())
        except FileNotFoundError:
            print("Файл с таким именем отсутствует в данной директории")
    elif a[0] == "ls":
        print("Содержимое папки:")
        print(os.listdir(t_dir))
    elif a[0] == "rm":
        try:
            os.remove(a[1])
        except FileNotFoundError:
            print("Файл с таким именем отсутствует в данной директории")
    else:
        print("Некорректная команда!")
