import math as m


def area(radius):
    return m.pi * radius * radius


def circumference(radius):
    return 2 * m.pi * radius


def diameter(radius):
    return 2 * radius


if __name__ == "__main__":
    try:
        rad = float(input("Enter value for radius (cm): "))
        print("Area:", area(rad))
        print("Circumference:", circumference(rad))
        print("Diameter:", diameter(rad))
    except ValueError:
        print("Please enter a valid numeric value for the radius.")
