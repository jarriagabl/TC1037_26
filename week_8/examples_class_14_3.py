def mean(lst):
    total = 0
    for value in lst:
        total += value
    return total / len(lst)

def max_value(lst):
    current_max = lst[0]
    for value in lst:
        if value > current_max:
            current_max = value
    return current_max

def main():
    lst1 = [12.5, 10.0, 13.5, 14.0]
    lst2 = [100, 78.0, 67.5, 90.5]
    lst3 = [100, 78.0, 125, 67.5, 90.5]
    print(f"Mean value of {lst1}: {mean(lst1)}")
    print(f"Mean value of {lst2}: {mean(lst2)}")
    print(f"Mean value of {lst3}: {mean(lst3)}")
    print(f"Max value of {lst1}: {max_value(lst1)}")
    print(f"Max value of {lst2}: {max_value(lst2)}")
    print(f"Max value of {lst3}: {max_value(lst3)}")

main()