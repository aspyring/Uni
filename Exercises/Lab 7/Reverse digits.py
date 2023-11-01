def reverse_digits(number):
    reversed_num = int(str(number)[::-1])
    digits = [int(digit) for digit in str(reversed_num)]
    return reversed_num, digits

def main():
    try:
        number = int(input("Enter a number between 1 and 9999: "))
        if 1 <= number <= 9999:
            reversed_num, reversed_digits = reverse_digits(number)
            print(f"The number with its digits reversed is: {reversed_num}")
        else:
            print("Please enter a number between 1 and 9999.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
