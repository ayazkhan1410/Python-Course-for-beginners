class Student: # parent
    def __init__(self,name,department,age,gender):
        self.name = name
        self.age = age
        self.department = department
        self.gender = gender
    def print_details(self):
        print("Name : ",self.name)
        print("Age : ", self.age)
        print("Department : ", self.department)
        print("Gender : ", self.gender)
class Teacher(Student):
    def __init__(self,name,age,department,gender,salary):
        super().__init__(name,age,department,gender)
        self.salary = salary
    def details(self):
        super().print_details()
        print("SALARY : ", self.salary)
# Creating an obejct
ss = Student("Ali",'IT',21,'Male')
ss.print_details()
tt = Teacher("Ayaz",21,"IT","Male",2500000)
tt.details()
