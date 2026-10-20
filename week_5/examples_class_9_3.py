def total_tax(income):
    if income <= 10000:
        tax_pct = 5
    elif income <= 20000:
        tax_pct = 15
    elif income <= 35000:
        tax_pct = 20
    elif income <= 60000:
        tax_pct = 30
    else:
        tax_pct = 45
    tax_due = income * (tax_pct/100)
    return tax_due

def main():
    income = int(input("Yearly income: "))
    tt = total_tax(income)
    print(f"The amount of taxes due is ${tt}")

main()
