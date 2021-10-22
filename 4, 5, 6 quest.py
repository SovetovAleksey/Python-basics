# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class Warehouse:
    pass


class OfficeEquipment:
    def __init__(self, name, price, number, *args):
        self.name = name
        self.price = price
        self.number = number
        self.units_dict = {'Название оргтехники': self.name, 'Цена - ': self.price, 'Количество -': self.number}
        self.units_list = []
        self.units_in_warehouse = []

    def distribution(self):
        while True:
            unit_name = input("Название оргтехники - ")
            unit_price = int(input("Цена за единицу - "))
            unit_mumbers = int(input("Количество единиц - "))
            units = {'Название': unit_name, 'Цена - ': unit_price, 'Количество -': unit_mumbers}
            self.units_dict.update(units)
            self.units_list.append(self.units_dict)
            print(f' Текущий список техники \n {self.units_list}')
            choice = input(f'Продолжить? Да/Нет ')

            if choice == "Да":
                return OfficeEquipment.distribution(self)

            elif choice == "Нет":
                self.units_in_warehouse.append(self.units_list)
                print(f"Техника на складе - {self.units_in_warehouse} \n")
                return f'Вы вышли'
            else:
                self.units_in_warehouse.append(self.units_list)
                print(f"Техника на складе - {self.units_in_warehouse}")
                return f'Вы вышли'


class Printer(OfficeEquipment):
    def __init__(self, model, name, price, number):
        super().__init__(name, price, number)
        self.model = model

    def to_print(self):
        return f'Распечатать'


class Scaner(OfficeEquipment):
    def __init__(self, model, name, price, number):
        super().__init__(name, price, number)
        self.model = model

    def to_scan(self):
        return f'Отсканировать'


class Xerox(OfficeEquipment):
    def __init__(self, model, name, price, number):
        super().__init__(name, price, number)
        self.model = model

    def to_xerox(self):
        return f'Отксерокопировать'


unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scaner('Canon', 1200, 5, 10)
unit_3 = Xerox('Xerox', 1500, 1, 15)
print(unit_1.distribution())
print(unit_1.to_print())
