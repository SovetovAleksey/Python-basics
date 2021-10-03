# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = int(input("Введите месяц "))

print("Через list")

month_list = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(month_list)

winter = month_list[0:3]
spring = month_list[3:6]
summer = month_list[6:9]
autumn = month_list[9:12]

if month in winter:
    print("Сейчас Зима")
elif month in spring:
    print("Сейчас Весна")
elif month in summer:
    print("Сейчас Лето")
elif month in autumn:
    print("Сейчас Осень")

print("Через dict")

month_dict = {"January":1, "February":2, "March":3,
              "April":4, "May":5, "June":6,
              "July":7, "August":8, "September": 9,
              "October": 10, "November": 11, "December":12
              }

print(month_dict)

if month == month_dict.get("December") or month == month_dict.get("January") or month == month_dict.get("February"):
    print("Сейчас Зима")
elif month == month_dict.get("March") or month == month_dict.get("April") or month == month_dict.get("May"):
    print("Сейчас Весна")
elif month == month_dict.get("June") or month == month_dict.get("July") or month == month_dict.get("August"):
    print("Сейчас Лето")
elif month == month_dict.get("September") or month == month_dict.get("October") or month == month_dict.get("November"):
    print("Сейчас Осень")