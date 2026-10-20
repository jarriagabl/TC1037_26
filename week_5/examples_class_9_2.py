def taxable(age, income):
    if age < 17 or income < 1000:
        return False
    else:
        return True

def main():
    user_age = int(input("Age: "))
    user_income = int(input("Monthly pay: "))
    if taxable(user_age, user_income):
        print("You should pay taxes")
    else:
        print("You don't need to pay taxes")

main()