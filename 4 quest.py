# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True if is_police else False
        self.direction = ''

    def go(self, speed):
        if speed > 0:
            print("Машина поехала вперед")
        elif speed < 0:
            print("Машина поехала назад")
        else:
            print("Машина стоит на месте")

    def stop(self, speed):
        if speed == 0:
            print("Машина остановилась\n")
        else:
            print("Машина не остановилась\n")

    def turn(self, direction):
        if direction == "left":
            print("Машина повернула налево")
        elif direction == "right":
            print("Машина повернула направо")

    def show_speed(self):
        print(f"Текущая скорость - {self.speed}км/ч")


class TownCar(Car):
    def __init__(self, *args):
        super().__init__(*args)

    def show_speed(self):
        if self.speed > 60:
            print(f"Текущая скорость - {self.speed}км/ч")
            print("Превышена скорость")
        else:
            print(f"Текущая скорость - {self.speed}км/ч")


class SportCar(Car):
    def __init__(self, *args):
        super().__init__(*args)


class WorkCar(Car):
    def __init__(self, *args):
        super().__init__(*args)

    def show_speed(self):
        if self.speed > 40:
            print("Превышена скорость")


class PoliceCar(Car):
    def __init__(self, *args):
        super().__init__(*args, is_police=True)


cybertruck = TownCar(80, "серый", "CyberTruck", False)
print(cybertruck.name)
cybertruck.go(20)
cybertruck.turn("left")
cybertruck.show_speed()
cybertruck.stop(30)

police_car = PoliceCar(100, "черный", "Ford Crown Victoria")
print(police_car.name)
police_car.go(-20)
police_car.turn("right")
police_car.show_speed()
police_car.stop(0)
