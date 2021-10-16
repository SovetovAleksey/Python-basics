# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).


class Worker():
    salary_dict = {}
    _income = salary_dict

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):

    def get_full_name(self):
        print(f"Полное имя - {self.name} {self.surname}")

    def get_total_income(self, wage, bonus):
        salary_dict = {"wage": wage, "bonus": bonus}
        total_income = salary_dict.get("wage") + salary_dict.get("bonus")
        print(f"Доход с учетом премии - {total_income}")


position_1 = Position("Иван", "Иванов", "Курьер")
position_1.get_full_name()
position_1.get_total_income(50000, 10000)

position_2 = Position("Сергей", "Симонов", "Продавец")
position_2.get_full_name()
position_2.get_total_income(100000, 20000)
