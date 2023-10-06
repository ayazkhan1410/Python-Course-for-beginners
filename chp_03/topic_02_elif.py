# marks_percentage = int(input("Enter your F.SC marks percentage : "))
# if marks_percentage>60 and marks_percentage<70:
#     print("You should take addmission in IUB")
# elif marks_percentage>70 and marks_percentage<80:
#     print("You should take addmission in BZU")
# elif marks_percentage>80 and marks_percentage<90:
#     print("You should take addmission in COMSATS")
# elif marks_percentage>90 and marks_percentage<=100:
#     print("You should take addmission in Punjab univeristy")
# else:
#     print("You should revise again")
number = 5
number2 = 7
print("Press 1 to take sum")
print("Press 2 to take substraction")
choice = int(input("Chose : "))
if choice == 1:
    print(number+number2)
elif choice == 2:
    print(number-number2)
else:
    print("Invalid choice")