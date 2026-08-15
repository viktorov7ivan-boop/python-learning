numbers = [5, 12, 7, 20, 3, 18, 11, 4]
even_numbers = []
odd_numbers = []
for n in numbers:
    if (n %2 == 0):
        even_numbers.append(n)
    else:
        odd_numbers.append(n)
print(even_numbers)
print(odd_numbers)

