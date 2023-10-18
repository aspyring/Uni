# xp > 5 , age > 30 , qual = true = interview
# age < 30 , qual = true xp > 5 = interview
# qual = false, xp > 5, age > 30 = interview
# qual = true, age > 30, xp < 5 = file
# qual = true, xp < 5, age < 30 = file
# xp > 5, qual = false, age < 30 =  file
# qual = false, xp < 5, age > 30 =  rejected
# qual = false, xp < 5, age < 30 = rejected

yrs = int(input("Enter the number of years of experience the candidate has: "))
age = int(input(f"\nEnter the age of the candidate: "))
qualified = str.lower(input(f"\nIs the candidate qualified? (Y/N): "))
if qualified == 'y':
    qq = 1
else:
    qq = 0

if (yrs > 5 and qq == 1) or (qq == 0 and yrs > 5) :
    print(f"\nCandidate will be called for an interview")
elif (qq == 1 and yrs < 5) or (qq == 0 and yrs > 5):
    print(f"\nKeep candidate in file")
elif (qq == 0 and yrs < 5):
    print(f"\nCandidate rejected.")



