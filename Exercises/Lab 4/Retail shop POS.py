pnum = int(input("Enter Product Number: "))
pamt = int(input("Enter Amount of Products: "))

match pnum:
    case 1:
        total = round((pamt * 5),4)
        print("Selected Product number: 1")
        print("Product unit price : RM5.00")
        print(f"Quantity sold : {pamt}")
        print(f"Total Price : {total}")
    case 2:
        total = round((pamt * 4.50),4)
        print("Selected Product number: 2")
        print("Product unit price : RM4.50")
        print(f"Quantity sold : {pamt}")
        print(f"Total Price : {total}")
    case 3:
        total = round((pamt * 2.99),4)
        print("Selected Product number: 3")
        print("Product unit price : RM2.99")
        print(f"Quantity sold : {pamt}")
        print(f"Total Price : {total}")
    case 4:
        total = round((pamt * 15.99),4)
        print("Selected Product number: 4")
        print("Product unit price : RM15.99")
        print(f"Quantity sold : {pamt}")
        print(f"Total Price : {total}")
    case 5:
        total = round((pamt * 59.99),4)
        print("Selected Product number: 5")
        print("Product unit price : RM59.99")
        print(f"Quantity sold : {pamt}")
        print(f"Total Price : {total}")
    case _:
        print("Invalid Product Number.")


