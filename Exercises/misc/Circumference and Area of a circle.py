import math
r = int(input("Input Radius: "))
C = round((math.pi * 2 * r), 2)
A = round((math.pi * r **2), 2)
print("Circumference:", C , "\nArea:", A)
print("Circumference: " + str(C) + "\nArea: " + str(A))
print(f"Circumference: {C} \nArea: {A}")