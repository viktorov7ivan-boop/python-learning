def divide(a, b):
    try:
        return int(a / b) 
        
    except ZeroDivisionError:
        return "На ноль делить нельзя"
print(divide(10, 2))
print(divide(10, 0))