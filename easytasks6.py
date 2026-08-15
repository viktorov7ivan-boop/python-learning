def get_discount(price):
    if price < 5000:
        return price
    elif 9999>price >= 5000:
        return price - (price * 5/100)
    else:
        return price - (price * 10/100)


print(get_discount(4000))
print(get_discount(7000))
print(get_discount(15000))