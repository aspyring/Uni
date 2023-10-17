mk = int(input("Enter your mark: "))
match mk:
    case mk if 80 <= mk <= 100:
        print("Grade: A")
    case mk if 60 <= mk <= 79:
        print("Grade: B")
    case mk if 40 <= mk <= 59:
        print("Grade: C")
    case mk if 0 <= mk <= 39:
        print("Grade: F")
    case _:
        print("Invalid Mark")