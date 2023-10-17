print("    Menu")
print("------------")
print("1. Python")
print("2. Java")
print("3. C#")
print("4. C")
fav = input("\nEnter your choice: ")

match fav:
    case "1":
        print("My favourite programming language is: Python")

    case "2":
        print("My favourite programming language is: Java")

    case "3":
        print("My favourite programming language is: C#")

    case "4":
        print("My favourite programming language is: C")

    case _:
        print("I do not have any favourite programming language")