students = {
    "John": 85,
    "Grace": 58,
    "Michael": 47,
    "Sarah": 91,
    "David": 73,
}

for name, score in students.items():
    if score >= 90:
        category = "Excellent"
    elif score >= 70:
        category = "Good"
    elif score >= 50:
        category = "Fair"
    else:
        category = "Fail"
    print(f"{name}: {score} → {category}")



customers = {
    "Alice": {"loyalty": True, "amount": 23000},
    "Bob": {"loyalty": False, "amount": 12000},
    "Mary": {"loyalty": True, "amount": 5400},
    "James": {"loyalty": False, "amount": 8800},
}

count = 0
print("Customers with Loyalty Cards:")
for name, info in customers.items():
    if info["loyalty"]:
        print("-", name)
        count += 1

print("Total with loyalty cards:", count)



orders = {
    "order1": 35000,
    "order2": 18000,
    "order3": 5000,
    "order4": 21000,
}

for order, amount in orders.items():
    if amount >= 20000:
        discount = 0.2
    elif amount >= 10000:
        discount = 0.1
    else:
        discount = 0.0

    final_price = amount * (1 - discount)
    print(f"{order}: Original = {amount}, Discounted = {final_price}")



spending = {
    "Tobi": 12000,
    "Sandra": 45000,
    "Chuka": 18000,
    "Faith": 29000
}

highest_name = ""
highest_amount = 0

for name, amount in spending.items():
    if amount > highest_amount:
        highest_amount = amount
        highest_name = name

print(f"Highest spender: {highest_name} → ₦{highest_amount}")



products = {
    "Rice": {"price": 1500, "stock": 30},
    "Beans": {"price": 1200, "stock": 12},
    "Oil": {"price": 4500, "stock": 5},
    "Tomato": {"price": 800, "stock": 0},
}

print("Available Products:\n")
for name, details in products.items():
    stock = details["stock"]
    price = details["price"]

    if stock > 0:
        total_value = price * stock
        print(f"{name} → Price: ₦{price}, Stock: {stock}, Value: ₦{total_value}")

