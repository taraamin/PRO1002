# Advanced Python Practice Tasks Work Requirement 2

# 1) File to List Converter

filename = input("Enter a filename to read: ").strip()

try:
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines()]
    print("Lines (stripped):", lines)
except FileNotFoundError:
    print("Error: file not found.")
except OSError as e:
    print(f"Error reading file: {e}")

# 2) Task List Manager

import tasks

task_list = []

while True:
    action = input("Type 'add <task>', 'remove <task>', or 'done': ").strip()

    if action.lower() == "done":
        print("Final tasks:", task_list)
        break
    elif action.lower().startswith("add "):
        task = action[4:]
        task_list = tasks.add_task(task_list, task)
    elif action.lower().startswith("remove "):
        task = action[7:]
        task_list = tasks.remove_task(task_list, task)
    else:
        print("Unknown command.")

    print("Current tasks:", task_list)

# 3) Simple class and Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hi, I'm {} and I'm {} years old.".format(self.name, self.age))

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

if __name__ == "__main__":
    name = input("Student name: ")
    age_text = input("Student age: ")
    sid = input("Student ID: ")

    try:
        age = int(age_text)
    except ValueError:
        print("Age must be a whole number.")
        raise SystemExit(1)

    s = Student(name, age, sid)
    s.greet()
    print("Student ID:", s.student_id)

# 4) Math quiz with Exception Handling
# Added else with the correct answer {a} + {b}

import random

a = random.randint(1, 10)
b = random.randint(1, 10)
print(f"Add these numbers: {a} + {b}")
ans_text = input("Your answer: ")

try:
    ans = int(ans_text)
    if ans == a + b:
        print("Correct!")
    else:
        print(f"Almost. The answer is actually {a + b}.")
except ValueError:
    print("Invalid input!")

# 5) Directory Lister
# try "." to test
    
import os

path = input("Enter a directory path: ").strip()

try:
    items = os.listdir(path)
    if not items:
        print("(Empty directory)")
    else:
        print("Contents:")
        for i, name in enumerate(items, start=1):
            print(f"  {i}. {name}")
except FileNotFoundError:
    print("Error: Directory not found.")
except PermissionError:
    print("Error: No permission to access this path.")
except OSError as e:
    print(f"OS error: {e}")
    

