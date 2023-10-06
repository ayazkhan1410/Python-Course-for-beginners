# class Father:
#     def skin_color(self):
#         print("Skin color : White")
#     def property(self):
#         print("4 marla property")
# class Brother(Father):
#     def heigth(self):
#         print("HEight is 5.6 ft")
# class Sister(Father):
#     def brain(self):
#         print("BIG BRAIN")
# # creating an object
# bb = Brother()
# bb.skin_color()
# bb.heigth()
# bb.property()
#
# ss = Sister()
# ss.skin_color()
# ss.brain()
# ss.property()

# another example
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def print_details(self):
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Gender : ", self.gender)
class Employee(Person):
    def __init__(self,name,age,gender,salary):
        super().__init__(name,age,gender)
        self.salary = salary
    def details(self):
        super().print_details()
        print("Salary : ", self.salary)
class Customer(Person):
    def __init__(self,name,age,gender,intrest):
        super().__init__(name,age,gender)
        self.intrest = intrest
    def print_details2(self):
        super().print_details()
        print("Customer intrest is in : ",self.intrest)

# creating an object
ee = Employee("Ayaz Khan",21,'Male',300000)
ee.details()

# creating another object
cc = Customer('AFFAN',22,'MALE','PROGRAMMING STICKERS')
cc.print_details2()