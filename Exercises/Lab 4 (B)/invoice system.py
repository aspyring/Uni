# If the amount of the order for the computer supplies is greater than $1000, give 4%
# discount for the order;
# • if the amount is between $500 and $1000, give 2% discount,
# • if the amount is less than $500, do not apply any discount.

days = int(input("Enter number of days taken to pay: "))
amt = int(input("Enter Order Amount: "))
if days <= 10:
    match amt:
        case amt if amt > 1000:
            finalamt = (0.96 * amt)
            print(f"Your Final Amount is : {finalamt}")
        case amt if 500 <= amt <= 1000:
            finalamt = (0.98 * amt)
            print(f"Your Final Amount is : {finalamt}")
        case amt if amt < 500:
            finalamt = amt
            print(f"Your Final Amount is : {finalamt}")
else:
    print(f"Your Final Amount is : {amt}")
