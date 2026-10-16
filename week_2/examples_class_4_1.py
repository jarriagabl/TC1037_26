# Area of a rectangle

# Remember: input() asks the user for a value,
# and returns it as a string. float() casts
# the string to a float (number)
base = float(input("Give me the base of the rectangle: "))
height = float(input("Give me the height of the rectangle: "))

area = base * height

# Remember: putting an f before the string turns it
# into an f-string (format string). Inside it, we
# can use {} to denote expressions
print(f"The area of the rectangle with base {base} and height {height} is {area:.2f}")