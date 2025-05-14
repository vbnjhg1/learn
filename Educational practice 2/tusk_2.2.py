# Создайте класс с именем Train, содержащий свойства: название пункта
# назначения, номер поезда, время отправления. Добавить возможность вывода
# информации о поезде, номер которого введен пользователем. Написать программу,
# демонстрирующую все возможности класса;
trains = []
def addTrains(train):
    trains.append(train)
class Train:
    def __init__(self, town_to, trainNum, time_from):
        self.__town_to = town_to
        self.__trainNum = trainNum
        self.__time_from = time_from
        addTrains(self)

    @property
    def trainNum(self):
        return self.__trainNum

    def __str__(self):
        return (f'Номер поезда: {self.__trainNum}\n'
                f'Место назначения - {self.__town_to}\n'
                f'Время отправки - {self.__time_from}\n')

def showTrains():
    for i in range(len(trains)):
        print(i + 1, trains[i])
showTrains()

def serchStudent():
    train = int(input("Введите номер поезда: "))
    for i in range(len(trains)):
        if train == trains[i].trainNum:
            print(trains[i])
            break
Sapsan = Train("Владикавказ", 1, '12:10')
Upiter = Train("Юпитер", 2, '12:30')
Hawk = Train("Гнездо", 3, '11:00')
showTrains()
serchStudent()
