# user age must be 18 or above to 18
# user weight must be 50 or up to 50
age = int(input("Enter your age : ")) #17
if age >= 18:
    w = int(input("Enter your weight : "))
    if w >= 50:
        print("You are eligible to donate blood")
    else:
        print("Please increase your weight ", 50 - w, "kg")
else:
    print("Your age is not full fill the requirement", 18 - age)


