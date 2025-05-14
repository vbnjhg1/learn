# Реализуйте класс Worker, который будет иметь следующие свойства: name,
# surname, rate (ставка за день работы), days (количество отработанных дней). Также класс
# должен иметь метод GetSalary(), который будет выводить зарплату работника. Зарплата -
# это произведение ставки rate на количество отработанных дней days;


workers = []
def addWorker(worker):
    workers.append(worker)
class Worker:
    def __init__(self, surname, name, rate, days):
        self.__surname = surname
        self.__name = name
        self.__rate = rate
        self.__days = days
        addWorker(self)

    def __str__(self):
        return (f'Работник: {self.__surname} {self.__name}\n'
                f'Ставка за день - {self.__rate}\n'
                f'Количество отработанных дней - {self.__days}\n')

    @property
    def surname(self):
        return self.__surname

    @property
    def name(self):
        return self.__name

    @property
    def rate(self):
        return self.__rate

    @property
    def days(self):
        return self.__days

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @name.setter
    def date_birth(self, name):
        self.__name = name

    @rate.setter
    def rate(self, rate):
        self.__rate = rate

    @days.setter
    def days(self, days):
        self.__days = days

    def getSalary(self):
        return self.__rate * self.__days
    def print_person(self):
        print(f"Фамилия: {self.__surname}\t  Дата Рождения: {self.__birthday}"
              f"\t Номер группы: {self.__groupe_num}\t оценки: {self.__grades}")

vasiliy = Worker("Вяльсиченко", "Таня", 550, 30)
print(vasiliy.__str__())
print(vasiliy.getSalary())