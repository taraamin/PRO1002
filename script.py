# 1. Age check and Greeting
name = input("Enter your name: ")
age_text = input("Enter your age: ")

try:
    age = int(age_text)
    if age >= 18:
        print(f"Hello, {name}! You can enter.")
    else:
        print(f"Sorry, {name}. You're too young.")
except ValueError:
    print("Age must be a whole number.")

print("-" * 50)

# 2. Number List Processor

n_text = input("Enter an integer n: ")
try:
    n = int(n_text)
    numbers = []
    for i in range(1, n + 1):
        numbers.append(i)
    print("List:", numbers)
    if n > 5:
        print("The list is long.")
    else:
        print("The list is short.")
except ValueError:
    print("Please enter a valid number.")

print("-" * 50)

# 3. Sum Userinput

vals = []
for i in range(1, 4):
    vals.append(input(f"Enter number {i}: "))

try:
    a, b, c = int(vals[0]), int(vals[1]), int(vals[2])
    total = a + b + c
    print("Numbers:", [a, b, c])
    print("Total:", total)
    if total % 2 == 0:
        print("Your sum is even!")
    else:
        print("Your sum is odd!")
except ValueError:
    print("All values must be integers.")

print("-" * 50)

# 4. Fruit Basket

basket = {"apple": 10, "banana": 5, "orange": 7, "pear": 3, "pomegranate": 4}
fruit = input("Which fruit do you want? ").strip().lower()

if fruit in basket:
    print(f"We have {basket[fruit]} {fruit}(s).")
    print("Letters in the fruit name:")
    for ch in fruit:
        print(ch)
else:
    print("We don't have that fruit.")

print("-" * 50)

#5. Temperature Converter
c_text = input("Enter temperature in Celsius: ")

try:
    c = float(c_text)  
    f = c * 9/5 + 32   
    print(f"Fahrenheit: {f}")

    if f > 80:
        print("It's hot!")
    else:
        print("It's not too hot.")

    temps = [c, f]
    print("[C, F] =", temps)
except ValueError:
    print("Please enter a number (e.g., 21 or 21.5).")

# 6. Menu Selection
menu = {"coffee": 10, "tea": 5, "juice": 7, "milkshake": 14}

item = input("What would you like to order? ").strip().lower()

if item in menu:
    print(f"{item.capitalize()} costs {menu[item]}.")
else:
    print("Item not found.")

print("Full menu:")
for k, v in menu.items():
    print(f" - {k.capitalize()}: {v}")

# 7. Number Analyzer

line = input("Enter numbers separated by spaces: ").strip()

if line:
    parts = line.split()
    numbers = []
    for p in parts:
        try:
            numbers.append(int(p))
        except ValueError:
            print("Invalid input, please enter numbers only.")
            numbers = []
            break

    if numbers:
        print("Numbers:", numbers)
        smallest = min(numbers)
        largest = max(numbers)
        average = sum(numbers) / len(numbers)
        print(f"Smallest: {smallest}, Largest: {largest}, Average: {average:.2f}")
        if average > 10:
            print("Average is high")
        else:
            print("Average is low")
else:
    print("No numbers entered.")

# 8. Letter Counter

word = input("Enter a word: ").strip().lower()

counts = {}
for ch in word:
    counts[ch] = counts.get(ch, 0) + 1

print("Letter counts:", counts)

if len(word) > 5:
    print("That's a long word!")

# 9. Guessing Game
secret = 1
guesses = []

while True:
    g = input("Guess the secret number: ")

    try:
        guess = int(g)
        guesses.append(guess)
        if guess == secret:
            print("You got it!")
            break
        else:
            print("Try again!")

    except ValueError:
        print("Please enter a whole number.")

print("Your guesses:", guesses)

# 10. Shopping List Manager

shopping_list = []

while True:
    item = input("Add an item to your shopping list (or type 'done'): ").strip()
    if item.lower() == "done":
        break
    if item:
        shopping_list.append(item)

print("Your shopping list:", shopping_list)

if len(shopping_list) > 3:
    print("You have a lot of items!")
else:
    print("You have a short list.")

