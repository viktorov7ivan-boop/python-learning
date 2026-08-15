student = {
    "name": "Иван",
    "grades": [5, 4, 3, 5, 4]
}
print(student["name"])
print(student["grades"])
total= sum(student["grades"])
count= len(student["grades"])
average = total / count
print(average)
if average >=4:
    print("Хорошая успеваемость")
else:
    print("Нужно подтянуть учебу")