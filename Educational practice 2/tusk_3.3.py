#  Создайте класс Calculation , в котором будет одно свойство calculationLine.
# методы: SetCalculationLine который будет который будет изменять значение свойства,
# SetLastSymbolCalculationLine который будет в конец строки прибавлять символ,
# GetCalculationLine который будет выводить значение свойства, GetLastSymbol получение
# последнего символа, DeleteLastSymbol удаление последнего символа из строки;
class Calculation:
    def __init__(self, calculationLine):
        self.calculationLine = calculationLine

    def __str__(self):
        return print(f'calculationLine: {self.calculationLine}')

    def SetCalculationLine(self, set):
        if type(set) == str:
            self.calculationLine = set
        else:
            print("Введите символы. Не число")

    def SetLastSymbolCalculationLine(self, set):
        if len(set) == 1:
            self.calculationLine += set
        else:
            print("Введите 1ин символ")
    def GetCalculationLine(self):
        print(f"{self.calculationLine}")

    def GetLastSymbol(self):
        print(self.calculationLine[-1])

    def DeleteLastSymbol(self):
        self.calculationLine = self.calculationLine[:-1]


vilage = Calculation("asdasd")
vilage.__str__()
vilage.SetCalculationLine("aфвавф")
vilage.SetLastSymbolCalculationLine("п")
vilage.GetCalculationLine()
vilage.GetLastSymbol()
vilage.DeleteLastSymbol()
vilage.GetCalculationLine()
