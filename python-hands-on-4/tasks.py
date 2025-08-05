 TASK 1: Student Score Classification
Dictionary:

students = {
    "John": 85,
    "Grace": 58,
    "Michael": 47,
    "Sarah": 91,
    "David": 73,
}
Goal:

Use a for loop and if-elif-else to classify:

90+ → "Excellent"

70–89 → "Good"

50–69 → "Fair"

Below 50 → "Fail"



✅ TASK 2: Count How Many Have Loyalty Cards
customers = {
    "Alice": {"loyalty": True, "amount": 23000},
    "Bob": {"loyalty": False, "amount": 12000},
    "Mary": {"loyalty": True, "amount": 5400},
    "James": {"loyalty": False, "amount": 8800},
}
Goal:

Count how many customers have loyalty = True

Print their names and the total count




✅ TASK 3: Apply Discounts Based on Amount
Dictionary:

orders = {
    "order1": 35000,
    "order2": 18000,
    "order3": 5000,
    "order4": 21000,
}
Goal:

If order is:

20000 → 20% discount

10000–20000 → 10% discount

else → no discount

Print the final price for each order





✅ TASK 4: Find the Highest Spender
spending = {
    "Tobi": 12000,
    "Sandra": 45000,
    "Chuka": 18000,
    "Faith": 29000
}
Goal:

Loop through the dict

Find and print the person with the highest spending and how much




✅ TASK 5: Build a Custom Summary
products = {
    "Rice": {"price": 1500, "stock": 30},
    "Beans": {"price": 1200, "stock": 12},
    "Oil": {"price": 4500, "stock": 5},
    "Tomato": {"price": 800, "stock": 0},
}
Goal:

Print all available products (stock > 0)

Skip out-of-stock items

For each available, print:

Product name, Price, Stock

Total value = price * stock
