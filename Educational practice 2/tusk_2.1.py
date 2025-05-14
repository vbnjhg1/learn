persons = []
def addPersons(person):
    persons.append(person)
class Student:
    def __init__(self, surname, birthday, groupe_num, grades):
        self.__surname = surname
        self.__birthday = birthday
        self.__groupe_num = groupe_num
        self.__grades = grades
        addPersons(self)

    def __str__(self):
        return f'Студент {self.__surname}:\nГод рождения - {self.__birthday}\nНомер группы - {self.__groupe_num}\nОценки - {self.__grades}\n'

    @property
    def surname(self):
        return self.__surname

    @property
    def date_birth(self):
        return self.__birthday

    @property
    def gr_num(self):
        return self.__groupe_num

    @property
    def grades(self):
        return self.__grades

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @date_birth.setter
    def date_birth(self, date_birth):
        if date_birth > 2000 and date_birth <= 2009:
            self.__birthday = date_birth

    @gr_num.setter
    def gr_num(self, gr_num):
        self.__groupe_num = gr_num

    @grades.setter
    def grades(self, grades):
        self.__grades = grades
    def print_person(self):
        print(f"Фамилия: {self.__surname}\t  Дата Рождения: {self.__birthday}"
              f"\t Номер группы: {self.__groupe_num}\t оценки: {self.__grades}")

prog_andr = [2, 3, 4, 4, 5]
prog_matw = [3, 3, 3, 3, 4]
prog_dany = [4, 3, 4, 3, 4]
andry = Student("Волков", 2006, 555, prog_andr)
matwey = Student("Балабанов", 2007, 645, prog_matw)
dany = Student("Безхозных", 2005, 535, prog_dany)

def showStudents():
    for i in range(len(persons)):
        print(i + 1, persons[i])
showStudents()

def serchStudent():
    surname = input("Введите фамилию студента: ")
    date_birth = int(input("Введите год рождения: "))
    for i in range(len(persons)):
        if surname == persons[i].surname and date_birth == persons[i].date_birth:
            print(persons[i])
            break

def dialog():
    print(f"Запустить редактор студентов - 1\nЗапустить поиск студента - 2")
    answer = int(input())
    if answer == 1:
        print("Напишите id студента:")
        id = int(input())
        if id-1 > len(persons):
            print("Не корректный id студента")
            dialog()
        else:
            print(f"Выбран студент: {persons[id-1].surname}\n"
                  f"Изменить фамилию - 1\n"
                  f"Изменить год рождения - 2\n"
                  f"Изменить номер групы - 3\n")
            Choice = int(input())
            if Choice == 1:
                persons[id - 1].surname = input("Введите фамилию ")
                showStudents()
                dialog()
            if Choice == 2:
                persons[id - 1].date_birth = int(input("Введите год рождения "))
                showStudents()
                dialog()
            if Choice == 3:
                persons[id - 1].gr_num = int(input("Введите номер групы "))
                showStudents()
                dialog()
    if answer == 2:
        serchStudent()
        dialog()

    else:
        print("Введено не корректное число.")
        dialog()
dialog()



