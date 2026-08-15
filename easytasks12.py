studients = [
    {
        "name": "Иван",
        "age": "18",
        "valuation": "5"
    },
    {
        "name": "Анна",
        "age": "19",
        "valuation": "4"
    },
    {
        "name": "Петр",
        "age": "18",
        "valuation": "3"
    }
]
for studient in studients:
    if studient["valuation"] >"3":
        print(f"{studient["name"]} - {studient["valuation"]}")