# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сумма с1 и с2 равна')
        if self.b + other.b > 0:
            return f'с = {self.a + other.a} + {self.b + other.b} * i'
        elif self.b + other.b < 0:
            return f'с = {self.a + other.a} - {(self.b + other.b) * (-1)} * i'

    def __mul__(self, other):
        print(f'Произведение с1 и с2 равно')
        if self.b * other.a > 0:
            return f'с = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'
        elif self.b * other.a < 0:
            return f'с = {self.a * other.a - (self.b * other.b)} - {(self.b * other.a) * (-1)} * i'

    def __str__(self):
        if self.b > 0:
            return f'с = {self.a} + {self.b} * i'
        elif self.b < 0:
            return f'с = {self.a} - {self.b * (-1)} * i'
        else:
            print("b не должно равняться 0 ")


c_1 = ComplexNumber(2, -5)
c_2 = ComplexNumber(1, 7)

print(c_1)
print(c_1 + c_2)
print(c_1 * c_2)
