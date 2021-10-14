# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from functools import reduce


def my_func(el, next_el):
    sum_el = int(el) + int(next_el)
    return sum_el


my_file = open("text", 'w+', encoding='utf-8')

new_numbers = input("Введите числа  через пробел: ")

my_file.write(new_numbers)

my_file.close()

with open('text', 'r') as fin:
    for line in fin:
        my_list = line.split()
        for el in my_list:
            ans = sum(int(el) for el in my_list)
    print(ans)

my_file.close()
