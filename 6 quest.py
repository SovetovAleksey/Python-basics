start = int(input("Первый результат спортсмена - "))
end = int(input("Чего нужно достичь - "))
day = 1

print(f"{day}-й день: {start}км")

while start < end:
    start = start * 1.1
    day += 1
    print(f"{day}-й день: {round(start, 2)}км")

print(f"На {day}-й день спортсмен достиг результата - не менее {end}км")
