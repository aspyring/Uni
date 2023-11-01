def parking_charge(hours_parked):
    if hours_parked <= 3:
        return 3.00
    elif hours_parked <= 20:
        additional_hours = hours_parked - 3
        charge = 3.00 + (additional_hours * 0.50)
        return min(charge, 12.00)
    else:
        return 12.00


def main():
    cars = []  # list to store information about cars

    for i in range(1, 6):
        hours = float(input(f"Hours - Car {i}: "))
        charge = parking_charge(hours)
        cars.append((i, hours, charge))  # store car information

    total = sum(charge for _, _, charge in cars)  # calc the total charges

    for i, hours, charge in cars:
        print(f"Hours - Car {i}: {hours:.2f}")
        print(f"Charge: RM{charge:.2f}")

    print(f"Total charges for the day: RM{total:.2f}")


if __name__ == "__main__":
    main()
