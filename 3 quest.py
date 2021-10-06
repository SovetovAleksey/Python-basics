# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func ():
    var_1 = int(input("Введите первое число "))
    var_2 = int(input("Введите второе число "))
    var_3 = int(input("Введите третье число "))

    var_list = [var_1, var_2, var_3]

    var_list.sort(reverse=True)

    res_sum = var_list[0] + var_list[1]

    return res_sum


print(my_func())


