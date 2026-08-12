d1 = {
    "C1": {
        "name": "YASH",
        "items": ["Notebook", "Pen", "Pencil"],
        "products": [
            ("Notebook", 80),
            ("Pen", 20),
            ("Pencil", 10)
        ],
        "categories": {"Writing", "Paper"}
    },
    "C2": {
        "name": "Vatsal",
        "items": ["Notebook", "Marker", "Eraser"],
        "products": [
            ("Notebook", 90),
            ("Marker", 60),
            ("Eraser", 15)
        ],
        "categories": {"Writing", "Paper"}
    },
    "C3": {
        "name": "Yash",
        "items": ["File", "Notebook", "Sketch Pen"],
        "products": [
            ("File", 70),
            ("Notebook", 100),
            ("Sketch Pen", 85)
        ],
        "categories": {"Paper", "Drawing"}
    }
}

highest_spent = 0
highest_customer = ""

for key, customer in d1.items():

    print("\nName:", customer["name"])
    print("Items:", customer["items"])

    total = 0
    highest_price = 0
    highest_item = ""
    expensive_items = set()

    for item, price in customer["products"]:

        total = total + price

        if price > highest_price:
            highest_price = price
            highest_item = item

        if price > 50:
            print("Above 50:", item, price)

        if price >= 80:
            expensive_items.add(item)

    print("Total:", total)
    print("Highest Item:", highest_item)
    print("80+ Items:", expensive_items)
    print("Notebook Present:", "Notebook" in customer["items"])

    if total > highest_spent:
        highest_spent = total
        highest_customer = customer["name"]

common = d1["C1"]["categories"] & d1["C2"]["categories"]

print("\nCommon Categories:", common)

d1["C1"]["items"].append("Pen")
d1["C1"]["products"].append(("Pen", 20))

print("\nUpdated Manav:")
print(d1["C1"])

print("\nHighest Spending Customer:", highest_customer)
print("Highest Spending:", highest_spent)