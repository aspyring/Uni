#Initialises the total
total = 0
noOfNums = int(input("Enter amount of numbers to calculate average: "))
#Loop to input Numbers
for x in range(noOfNums):
    num = int(input("Enter number " + str(x + 1) + ": "))
    total = total + num

#Calculates average of the specified number of numbers and prints it.
avg = total / noOfNums
print("The average of the " + str(noOfNums) + " numbers is: " + str(avg))
