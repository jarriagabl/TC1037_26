import math

def print_message():
    print("Processing...")
    print("Still processing...")

def print_other_message():
    print("Wait for it...")

print_other_message()
print_message()
print_message()

def rectangle_area(width, height):
    area = width * height
    return area

def circle_area(radius):
    return math.pi * (radius ** 2)

def total_rectangle_area(w1, h1, w2, h2):
    a1 = rectangle_area(w1, h1)
    a2 = rectangle_area(w2, h2)
    return a1 + a2

print(f"The area of a rectangle of width 4 and height 5 is {rectangle_area(4, 5)}")
print(f"The area of a circle with radius 5 is {circle_area(5):.4f}")
print(f"The total area of a shape composed of two rectangles of 4 by 5 and 3 by 8 is {total_rectangle_area(4, 5, 3, 8)}")