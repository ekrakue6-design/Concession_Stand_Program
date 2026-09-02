# Concession stand program

menu = {"Bread": 3.90,
        "Carrot":4.00,
        "Kfc":29.00,
        "Fries":6.00,
        "sweet":6.00,
        "lemon":9.00,
        "Toothpaste": 4.89}

cart =[]
total = 0


print("----------MENU--------")
for key, value in menu.items():
    print(f"{key:10}: {value:.2f}")
print("-----------------------")


while True:
        food = input("select an item (q to quit): ")
        if food == "q":
            break
        elif menu.get(food) is not None:
                cart.append(food)
print(cart)
print("-----------YOUR ORDER----------")
for food in cart:
        total += menu.get(food)
        print(food , end = " ")

print()
print(f"total: ${total:.2f}")