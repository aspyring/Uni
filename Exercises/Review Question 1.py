#Initialises the total variable
total = 0
#Loop to input Numbers
for x in range(5):
    num = int(input("Enter number " + str(x + 1) + ": "))
    total = total + num
#Calculates average of the specified number of numbers and prints it.
avg = total / 5
print("The average of the 5 numbers is: " + str(avg))
