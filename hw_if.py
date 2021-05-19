age = abs(int(input("Введите ваш возраст: ")))

def user_age(age):
    if age <= 6:
        return("Ты долден быть в саду")
    elif age >= 8 and age < 19:
        return("Ты должен быть в школе")
    elif age >= 19 and age < 26:
        return("Ты должен быть в ВУЗе")
    elif age >= 26:
       return("Ты должен работать")

value = user_age(age)
print(value)

