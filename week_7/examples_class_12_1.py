def balance():
    total_balance = 0 # acumulator
    num_months = 0 # counter
    while total_balance < 1000:
        money_saved_this_month = float(input("How much did you save this month? "))
        total_balance += money_saved_this_month
        num_months += 1
    print(f"You saved a total of ${total_balance:.2f} and it took you {num_months} months")

balance()