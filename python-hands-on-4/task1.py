#Task 1: Music Concert Ticketing System
#During the Jos Summer Music Concert, ticket sales were recorded as follows:
t#ickets = {"VIP": 50, "Regular": 150, "Student": 75}
#Later in the day:
#- A new "Backstage" experience with 10 tickets was introduced.
#- The "Student" category sold out complete- The team wanted to keep a record of
the day’s sales before preparing for next week’s concert.
# JOS SUMMER MUSIC CONCERT TICKETING SYSTEM

# JOS SUMMER MUSIC CONCERT TICKETING SYSTEM

# Step 1: Initial ticket sales record
tickets = {
    "VIP": 50,
    "Regular": 150,
    "Student": 75
}

# Step 2: Later in the day...
# Add a new ticket category: Backstage
tickets["Backstage"] = 10

# Student tickets sold out
tickets["Student"] = 0

# Step 3: Make a copy of the day's sales
todays_sales = tickets.copy()

# Step 4: Display today's updated ticket records
print("\nToday's Sales Record:")
print("-" * 30)
for category, count in todays_sales.items():
    print(f"{category:<10}: {count} ticket(s)")
print("-" * 30)

# Step 5: Calculate total tickets sold
total_sold = sum(todays_sales.values())
print(f"Total Tickets Sold Today: {total_sold}")

