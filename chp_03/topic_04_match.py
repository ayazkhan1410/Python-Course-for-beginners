# num1 = int(input("Enter number one : "))
# num2 = int(input("Enter number two : "))
# print("Press 1 to take sum")
# print("Press 2 to take substraction")
# choice = int(input("Choise : "))
# match choice:
#     case 1:
#         print("The sum is : ", num1+num2)
#     case 2:
#         print("The substraction is : ", num1-num2)
#     case _:
#         print("Invalid choice")

number = int(input("Enter number between 1 and 5 : "))
match number:
    case 1:
        print("You chose 1")
    case 2:
        print("You chose 2")
    case 3:
        print("You chose 3")
    case 4:
        print("You chose 4")
    case 5:
        print("You chose 5")
    case _:
        print("Please chose number between 1 and 5")