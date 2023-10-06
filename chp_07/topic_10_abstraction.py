from math import pi
class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        print(f"The Area of Rectangle is : {self.length*self.width}")
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print(f"The Area of Circle is : {self.radius*self.radius * pi}")
i = True
while i:
    print("Press 1 to calculate area of Rectangle")
    print("Press 2 to calculate area of Circle")
    choice = int(input("Choice : "))
    if choice == 1:
        length = 0.0
        width = 0.0
        length = float(input("Enter Length : "))
        width = float(input("Enter width : "))
        rr = Rectangle(length,width)
        rr.area()
    elif choice == 2:
        radius = 0.0
        radius = float(input("Enter radius :"))
        cc = Circle(radius)
        cc.area()
    else:
        print("Invalid Input")
    user_input = input("Would you like to continue : y/n : ")
    if user_input == 'y'.lower():
        i = True
    else:
        i = False
        print("Thank you for using our program")
        break

