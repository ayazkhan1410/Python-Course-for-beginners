class Student:
    def __init__(self,name,age,gender,semester):
        self.name = name
        self.age = age
        self.gender = gender
        self.semester = semester
    def print_details(self):
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Gender : ", self.gender)
        print("Semester : ",self.semester)
# creating an object
name = input("Enter your name : ")
age = int(input("Enter your age : "))
gender = input("Enter your gender : ")
semester = input("Enter your semester : ")

ss = Student(name,age, gender,semester)
ss.print_details()

ss2 = Student('ali',21,'male','6th')
ss2.print_details()



