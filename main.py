# file = open("TEST1.py", "r")
# print(file.read())
# file.close()

with open("TEST1.py", 'r') as file:
    for line in file:
        print(line.strip())

with open("")