# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func_1(word):
    caps = []
    caps.append(word[0].upper())
    caps.append(word[1:])
    str1 = ''.join(caps)
    return str1


print(int_func_1("слово"))


def int_func_2(words):
    caps = []
    words_split = words.split(' ')
    for i, items in enumerate(words_split):
        caps.append(int_func_1(words_split[i]))
    str2 = ' '.join(caps)
    return str2


print(int_func_2("произвольный набор слов"))
