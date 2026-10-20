# Two ways to solve the same problem

age = int(input("Please give me your age: "))
if age < 18:
    print("Underage")
else:
    print("Adult")

age = int(input("Please give me your age: "))
if age >= 18:
    print("Adult")
else:
    print("Underage")

