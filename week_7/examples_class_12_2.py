def add_this_up():
    total = 0
    num = int(input("Give me a number (0 to stop): "))
    while num != 0:
        total += num # total = total + num
        num = int(input("Give me a number (0 to stop): "))
    return total

def give_me_a_positive():
    num = int(input("Give me a positive value: "))
    while num < 0:
        print("Read carefully...")
        num = int(input("Give me a positive value: "))
    return num

def password(pw):
    guess = input("Password: ")
    t = 1
    while guess != pw:
        print("Access denied")
        guess = input("Password: ")
        t += 1
    print(f"Access granted after {t} tries")

def main():
    # Testing add_this_ip
    t = add_this_up()
    print(f"The total is {t}")
    
    # Testing give_me_a_positive
    n = give_me_a_positive()
    print(n)
    
    # Testing password checker
    password("pass123")
    
main()