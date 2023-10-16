# Start​
#
# Prompt user for min and max temperature ​
#
# Read min_temp, max_temp ​
#
# Calculate avg_temp = (min_temp + max_temp) / 2 ​
#
# Display avg_temp ​
#
# End

min = int(input("Enter Minimum Temperature: "))
max = int(input("Enger Maximum Temperature: "))
avg = round(((min +max) / 2),2)
print(f"Average Temperature: {avg}")