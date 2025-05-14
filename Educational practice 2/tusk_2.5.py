
# Создать класс с двумя свойствами. Добавить конструктор с входными
# параметрами. Добавить конструктор, инициализирующий свойства по умолчанию.
# Добавить деструктор, выводящий на экран сообщение об удалении объекта. Написать
# программу, демонстрирующую все возможности класса;

class twoVariables:

    def __init__(self, first=1, second=2):
        self.__first = first
        self.__second = second

    def __str__(self):
        return print(f"{self.__first}, {self.__second}")

    def __del__(self):
        print("Экземпляр класса удалён")


one = twoVariables(1,62)
two = twoVariables()

one.__str__()
two.__str__()

del one
del two