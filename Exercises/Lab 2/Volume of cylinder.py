import math
r = int(input("Please enter radius: "))
h = int(input("Please enter Height: "))
Vol = round((math.pi * r ** 2 * h), 2)
lsa = round((2 * math.pi * r * h), 2)
tsa = round((2 * math.pi * r * (r + h)), 2)
print(f"Volume for the circular cylinder is: {Vol} \nLateral surface area is: {lsa} \nTotal Surface Area is: {tsa}")

