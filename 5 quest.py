proceeds = int(input("Укажите выручку вашей фирмы "))
costs = int(input("Укажите траты вашей фирмы "))

if proceeds > costs:
    print("Ваша фирма получает прибыль ")
    rent = (proceeds - costs) / proceeds
    employees = int(input("Укажите численность ваших сотрудников "))
    employ_cost = costs / employees
    result = proceeds - employ_cost
    print(f"Прибыль в расчет одного сотрудника - {result}")
else:
    print("Ваша фирма находится в убытке ")
