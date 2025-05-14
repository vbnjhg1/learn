# Описать класс, реализующий счетчик, который может увеличивать или
# уменьшать свое значение на единицу. Предусмотреть инициализацию счетчика со
# значением по умолчанию и произвольным значением. Счетчик имеет два метода:
# увеличения и уменьшения, — и свойство, позволяющее получить его текущее состояние.
# Написать программу, демонстрирующую все возможности класса;

class Counter:

    def __init__(self, number):
        self.__number = number

    def __str__(self):
        return (f"{self.__number}")

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number

def add():
    num.number += 1

def subtract():
    num.number -= 1

num = Counter(0)

def dialog():
    choice = input("Что бы установить свое значение для счётчика, введите 1\n"
                   "Что бы прибавить 1, введите '+'\n"
                   "Что бы убавить 1, Введите '-'\n")
    if choice == "1":
        print(f"Сейчас счётчик = {num.number}")
        num.number = int(input("Введите значение счётчика\n"))
        dialog()
    if choice == "+":
        add()
        print(f"Cчётчик = {num.number}")
        dialog()
    if choice == "-":
        subtract()
        print(f"Cчётчик = {num.number}")
        dialog()
    else:
        print("Введите корректное значение.")
        dialog()
dialog()