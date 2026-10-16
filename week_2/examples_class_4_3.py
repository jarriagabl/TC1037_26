# Multiplication of two numbers
num1 = float(input("Give me a number: "))
num2 = float(input("Give ma another number: "))

# There are several ways in which we can produce
# the result, for instance store the value in a
# variable and then print out the variable
result = num1 * num2
print(f"The result of the operation is {result}")

# or skip the variable and directly calculate the result
# as the argument for the print function
print("The result of the operation is", num1 * num2)
# or as an expression inside an f-string
print(f"The result of the operation is {num1 * num2}")

