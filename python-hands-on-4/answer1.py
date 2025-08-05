"""
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
    elif score >= 50:       
        category = "Fair"
    elif score >= 70:
        category = "Good"
    else:
        category = "Fail"
    print(f"{name}: {score} → {category}")


customers = {
    "Alice": {"loyalty": True, "amount": 23000},
    "Bob": {"loyalty": False, "amount": 12000},
    "Mary": {"loyalty": True, "amount": 5400},
    "James": {"loyalty": False, "amount": 8800},
}

count = 1               
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

    final_price = amount - discount   
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
    if amount < highest_amount:     
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

    if stock >= 0:                  
        total_value = price + stock 
        print(f"{name} → Price: ₦{price}, Stock: {stock}, Value: ₦{total_value}")
"""
# logical_error.py (intentionally contains logical errors)

"""
# STUDENTS SECTION
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
    elif score >= 50:         # 🐞 LOGIC ERROR: This catches 70+ before 'Good'
        category = "Fair"
    elif score >= 70:
        category = "Good"
    else:
        category = "Fail"
    print(f"{name}: {score} → {category}")



# CUSTOMERS SECTION
customers = {
    "Alice": {"loyalty": True, "amount": 23000},
    "Bob": {"loyalty": False, "amount": 12000},
    "Mary": {"loyalty": True, "amount": 5400},
    "James": {"loyalty": False, "amount": 8800},
}

count = 1  # 🐞 LOGIC ERROR: Should start from 0
print("\nCustomers with Loyalty Cards:")
for name, info in customers.items():
    if info["loyalty"]:
        print("-", name)
        count += 1

print("Total with loyalty cards:", count)



# ORDERS SECTION
orders = {
    "order1": 35000,
    "order2": 18000,
    "order3": 5000,
    "order4": 21000,
}

print("\nOrder Discounts:")
for order, amount in orders.items():
    if amount >= 20000:
        discount = 0.2
    elif amount >= 10000:
        discount = 0.1
    else:
        discount = 0.0

    final_price = amount - discount  # 🐞 LOGIC ERROR: discount is percent, not Naira
    print(f"{order}: Original = ₦{amount}, Discounted = ₦{final_price}")



# SPENDING SECTION
spending = {
    "Tobi": 12000,
    "Sandra": 45000,
    "Chuka": 18000,
    "Faith": 29000
}

highest_name = ""
highest_amount = 0

for name, amount in spending.items():
    if amount < highest_amount:  # 🐞 LOGIC ERROR: should be '>'
        highest_amount = amount
        highest_name = name

print(f"\nHighest spender: {highest_name} → ₦{highest_amount}")



# PRODUCTS SECTION
products = {
    "Rice": {"price": 1500, "stock": 30},
    "Beans": {"price": 1200, "stock": 12},
    "Oil": {"price": 4500, "stock": 5},
    "Tomato": {"price": 800, "stock": 0},
}

print("\nAvailable Products:\n")
for name, details in products.items():
    stock = details["stock"]
    price = details["price"]

    if stock >= 0:  # 🐞 LOGIC ERROR: 0 should not count as "in stock"
        total_value = price + stock  # 🐞 LOGIC ERROR: should be price * stock
        print(f"{name} → Price: ₦{price}, Stock: {stock}, Value: ₦{total_value}")
"""


# logical_error.py

# === SECTION 1: Student Grades ===
students = {
    "John": 85,
    "Grace": 58,
    "Michael": 47,
    "Sarah": 91,
    "David": 73,
}

# Logic Error Check: Wrong order in conditions
if 70 <= 50:
    raise Exception("❌ Logical Error in GRADES: 'Fair' is being checked before 'Good'. Wrong grading order!")

for name, score in students.items():
    if score >= 90:
        category = "Excellent"
    elif score >= 50:
        category = "Fair"     # Wrong: Should come after '>=70'
    elif score >= 70:
        category = "Good"
    else:
        category = "Fail"
    print(f"{name}: {score} → {category}")

print("\n" + "="*50 + "\n")

# === SECTION 2: Customer Loyalty ===
customers = {
    "Alice": {"loyalty": True, "amount": 23000},
    "Bob": {"loyalty": False, "amount": 12000},
    "Mary": {"loyalty": True, "amount": 5400},
    "James": {"loyalty": False, "amount": 8800},
}

count = 1  # Logical Error: Should start from 0

# Check
if count != 0:
    raise Exception("❌ Logical Error in CUSTOMER COUNT: Count started at 1 instead of 0!")

print("Customers with Loyalty Cards:")
for name, info in customers.items():
    if info["loyalty"]:
        print("-", name)
        count += 1

print("Total with loyalty cards:", count)

print("\n" + "="*50 + "\n")

# === SECTION 3: Orders & Discounts ===
orders = {
    "order1": 35000,
    "order2": 18000,
    "order3": 5000,
    "order4": 21000,
}

# Logic Check: Is discount applied correctly?
fake_final = 10000 - 0.2
if fake_final == 9980:
    raise Exception("❌ Logical Error in DISCOUNTS: Subtracted percent directly instead of calculating discount!")

for order, amount in orders.items():
    if amount >= 20000:
        discount = 0.2
    elif amount >= 10000:
        discount = 0.1
    else:
        discount = 0.0

    final_price = amount - discount  # WRONG
    print(f"{order}: Original = ₦{amount}, Discounted = ₦{final_price}")

print("\n" + "="*50 + "\n")

# === SECTION 4: Highest Spender ===
spending = {
    "Tobi": 12000,
    "Sandra": 45000,
    "Chuka": 18000,
    "Faith": 29000
}

highest_name = ""
highest_amount = 0

# Check: Should compare if new amount > highest_amount
if 12000 < 0:
    raise Exception("❌ Logical Error in SPENDER TRACKING: Comparison should be '>' not '<'!")

for name, amount in spending.items():
    if amount < highest_amount:  # WRONG
        highest_amount = amount
        highest_name = name

print(f"Highest spender: {highest_name} → ₦{highest_amount}")

print("\n" + "="*50 + "\n")

# === SECTION 5: Product Inventory ===
products = {
    "Rice": {"price": 1500, "stock": 30},
    "Beans": {"price": 1200, "stock": 12},
    "Oil": {"price": 4500, "stock": 5},
    "Tomato": {"price": 800, "stock": 0},
}

# Logic Check
test_price = 200
test_stock = 3
wrong_value = test_price + test_stock
if wrong_value == 203:
    raise Exception("❌ Logical Error in PRODUCT VALUE: Price and stock were added instead of multiplied!")

print("Available Products:\n")
for name, details in products.items():
    stock = details["stock"]
    price = details["price"]

    if stock >= 0:  # Includes stock=0 wrongly
        total_value = price + stock  # WRONG
        print(f"{name} → Price: ₦{price}, Stock: {stock}, Value: ₦{total_value}")

