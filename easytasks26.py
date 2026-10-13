sum2 = 0
sum1 = 0
positive = 0
maximum = 0

while True:
    counter = int(input("Your number: "))

    if counter < 0:
        continue
    elif counter == 0:
        break
    else:
        positive += 1
        
        if counter %2 == 0:
            sum2 += counter
        else:
            sum1 += counter
            

        
        if counter > maximum:
            maximum = counter 

if positive == 0:
    print("Положительных чисел не было")
else:
    print("Сумма четных:",sum2)
    print("Сумма нечетных:",sum1)
    print("Количество положительных:",positive)
    print("Максимальное число:",maximum)