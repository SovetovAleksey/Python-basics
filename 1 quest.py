# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, day, month, year):
        self.day = str(day)
        self.month = str(month)
        self.year = str(year)

    @classmethod
    def extract(cls, day, month, year):
        my_data = []

        my_data.append(day)
        my_data.append(month)
        my_data.append(year)

        print(int(my_data[0]), int(my_data[1]), int(my_data[2]))

    @staticmethod
    def valid(day, month, year):
        if day > 31:
            print("Введен не правильный день!")
        elif month > 12:
            print("Введен не правильный месяц!")
        elif year > 2021:
            print("Введен не правильный год!")

    def __str__(self):
        return f'Дата - {Data.extract(self.day, self.month, self.year)}'


Data.extract(2, 6, 1997)
Data.valid(2, 6, 1997)
Data.valid(55, 6, 1997)
Data.valid(2, 18, 1997)
Data.valid(2, 6, 2056)
