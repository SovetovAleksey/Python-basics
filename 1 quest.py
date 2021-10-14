# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

text_data = input("Введите данные ")

while text_data != "":
    my_file = open("first_text.txt", 'a', encoding='UTF-8')
    my_file.write(text_data + '\n')

    my_file.close()

    text_data = input("Введите данные ")

my_file = open("first_text.txt", 'r')
content = my_file.read()

print(content)

my_file.close()
