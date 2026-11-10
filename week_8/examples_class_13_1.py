def odds_and_evens(stopping):
    number = 0
    while number < stopping:
        if number % 2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")
        number += 1

def count_and_sum():
    count = 0
    total_sum = 0
    num = int(input("Give me a number (0 to stop): "))
    while num != 0:
        total_sum += num
        count += 1
        num = int(input("Give me a number (0 to stop): "))
    print(f"The total sum of the {count} values is {total_sum}")


