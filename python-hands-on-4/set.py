# Numbers list
numbers = [12, 45, 3, 89, 22]

print("📊 Numbers List:", numbers)
print("🔺 Maximum number:", max(numbers))
print("🔻 Minimum number:", min(numbers))
print()

# Strings list (names)
names = ["Zara", "Alice", "John", "Bob"]

print("👥 Names List:", names)
print("🔺 Name that comes last alphabetically:", max(names))
print("🔻 Name that comes first alphabetically:", min(names))
print()

# 🎮 User input example
print("🎮 Let's try it yourself!")

user_nums = input("Enter 5 numbers separated by spaces: ")
user_list = [int(n) for n in user_nums.split()]

print("✅ You entered:", user_list)
print("🔺 Max:", max(user_list))
print("🔻 Min:", min(user_list))

