# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class Exeption():
    def __init__(self, value):
        self.value = value

    def exept_zero(self):
        try:
            result = 100 / self.value
        except ZeroDivisionError:
            print("Делить на ноль нельзя!")
        else:
            print(f"Ответ - {result}")
        finally:
            print("Программа завершена")


point_1 = Exeption(1)
point_2 = Exeption(0)
point_1.exept_zero()
point_2.exept_zero()