products = [
    {"name": "iPhone", "price": 70000},
    {"name": "Samsung", "price": 55000},
    {"name": "Poco", "price": 25000},
]
def show_expensive(products):
    for product in products:
        if product["price"] > 50000:
            print(f"{product["name"]} - {product["price"]}")
show_expensive(products)
            