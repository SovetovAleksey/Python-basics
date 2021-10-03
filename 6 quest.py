k = 1

name = input("Введите название товара ")
cost = input("Введите стоимость товара ")
number = input("Введите количество товара ")
unit = input("единица измерения товара ")

product_dict = {"Название": name, "Цена": cost, "Количество": number, "ед.": unit}

product_tuple = (k, product_dict)

product_list = [product_tuple]

names = [name]
costs = [cost]
numbers = [number]
units = [unit]

product_dict_2 = {"Название": names, "Цена": costs, "Количество": numbers, "Единца измерения": units}
product_list_2 = [product_dict_2]

while True:

    k = k + 1

    ask = input("Товары закончились?(Да/Нет) ")
    if ask == "Нет":
        name = input("Введите название товара ")
        cost = input("Введите стоимость товара ")
        number = input("Введите количество товара ")
        unit = input("единица измерения товара ")

        product_dict = {"Название": name, "Цена": cost, "Количество": number, "ед.": unit}

        product_tuple = (k, product_dict)

        product_list.append(product_tuple)

        names.append(name)
        costs.append(cost)
        numbers.append(number)
        units.append(unit)

    elif ask == "Да":
        break

print(*product_list, sep='\n')
print(*product_dict_2.items(), sep='\n')
