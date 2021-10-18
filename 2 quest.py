# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Cloth():

    @abstractmethod
    def consumption_1(self, V):
        pass

    @abstractmethod
    def consumption_2(self, H):
        pass


class Coat(Cloth):

    def __init__(self, V):
        self.V = V

    def consumption_1(self, **kwargs):
        consumption_1 = self.V / 6.5 + 0.5
        print(f"Расход ткани на пальто - {consumption_1}")


class Costume(Cloth):

    def __init__(self, H):
        self.H = H

    def consumption_2(self, **kwargs):
        consumption_2 = 2 * self.H + 0.3
        print(f"Расход ткани на костюм - {consumption_2}")


coat = Coat(5)
coat.consumption_1()
costume = Costume(10)
costume.consumption_2()
