# Создайте класс с двумя свойствами для хранения целых чисел. Добавить
# метод для вывода на экран и метод для изменения этих чисел. Добавить метод, который
# находит сумму значений этих чисел, и метод который находит наибольшее значение из
# этих чисел. Написать программу, демонстрирующую все возможности класса;
numbers = []
def addNumber(number):
    numbers.append(number)
class Number:
    def __init__(self, number):
        self.__number = number
        addNumber(self)

    def __str__(self):
        return (f"{self.__number}")

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number

first = Number(10)
second = Number(15)


def getSum():
    print(numbers[0].number + numbers[1].number)


def getMaxNum():
    print(max(numbers[0].number, numbers[1].number))

def showNums():
    for i in range(len(numbers)):
        print(numbers[i])
showNums()

def editNums():
    first = int(input("Введите первое число "))
    second = int(input("Введите второе число "))
    numbers[0].number = first
    numbers[1].number = second
def dialog():

    Choice = int(input(f"Что бы изменить числа, введите 1\n"
                       f"Что бы найти наибольшее из чисел, введите 2\n"
                       f"Что бы найти сумму двух чисел, введите 3\n"))
    if Choice == 1:
        editNums()
        dialog()
    if Choice == 2:
        getMaxNum()
        dialog()
    if Choice == 3:
        getSum()
        dialog()
dialog()
