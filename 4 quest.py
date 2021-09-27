value = int(input("Введите число "))

max = value % 10
value = value // 10
while value > 0:
    if max < value % 10:
        max = value % 10
    value = value // 10

print(max)
