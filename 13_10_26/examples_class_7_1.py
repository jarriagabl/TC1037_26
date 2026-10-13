import math

def area_cylinder(radius, height):
    return (2 * math.pi * radius ** 2) + (2 * math.pi * radius * height)

def volume_cylinder(radius, height):
    return math.pi * (radius ** 2) * height

def main():
    radius = float(input("Radius of the cylinder: "))
    height = float(input("Height of the cylinder: "))
    area = area_cylinder(radius, height)
    volume = volume_cylinder(radius, height)
    print(f"Given the cylinder with height {height} and radius {radius}, the area is {area:.4f} and the volume is {volume:.4f}")

main()