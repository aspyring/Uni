def calc_earnings(sales):
    salary = 100.00
    commission = 0.15 * sales
    earnings = salary + commission
    return earnings

def main():
    while True:
        try:
            sales_input = input("Enter sales (-1 to end): ")
            sales = float(sales_input.replace("RM", ""))
            if sales == -1:
                break
            earnings = calc_earnings(sales)
            print(f"Salary is RM{earnings:.2f}")
        except ValueError:
            print("Please enter a valid numeric value for sales.")

if __name__ == "__main__":
    main()
