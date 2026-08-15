def check_age(age):
    if age < 0:
        print("Некорректный возраст")
    elif age <18:
        print("Доступ запрещен")
    elif 18<=age<=64:
        print("Доступ разрешен")
    else: 
        print("Льготный доступ")
check_age(15)
check_age(30)
check_age(70)

