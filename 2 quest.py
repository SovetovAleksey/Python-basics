time = int(input("Укажите время в секундах "))

hour = time // 3600
minute = (time - (hour * 3600)) // 60
sec = time - hour * 3600 - minute * 60

print(f"{hour}:{minute}:{sec}")