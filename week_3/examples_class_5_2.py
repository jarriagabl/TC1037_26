total_bill = float(input("What was the bill total? "))
tip_pct = float(input("What percentage would you like to leave as a tip? (1 - 100) "))
tip_total = (total_bill * tip_pct) / 100
print(f"The tip total is ${tip_total:.2f}")