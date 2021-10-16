# 2. Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500т

class Road():
    mass = 25
    height = 5

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def formula(self):
        result = self._length * self._width * self.mass * self.height
        result = result / 1000  # перевод в тонны
        print(f"{self._length}м * {self._width}м * {self.mass}кг * {self.height}см = {result}т")


asphalt = Road(20, 5000)
asphalt.formula()
