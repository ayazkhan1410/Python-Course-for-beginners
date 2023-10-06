class Scholarship:
    #class variables
    name = " "
    _semester = 0
    __cgpa = 0.00

    @property
    def getName(self):
        return self.name
    @getName.setter
    def setName(self,name):
        self.name = name
    @property
    def getSemester(self):
        return self._semester
    @getSemester.setter
    def setSemester(self,semester):
        if semester >= 6:
            self._semester = semester
        else:
            self._semester = semester
            print("You are not eligible for this scholarship")
    @property
    def getCgpa(self):
        return self.__cgpa
    @getCgpa.setter
    def setCgpa(self,cgpa):
        if cgpa >= 3.00:
            self.__cgpa = cgpa
        else:
            self.__cgpa = cgpa
            print("You are not eligible for this scholarship")
# creating an object
ss = Scholarship()
name = input("Enter your name : ")
ss.setName = name
semester = int(input("Enter your semester : "))
ss.setSemester = semester
cgpa = float(input("Enter your cgpa : "))
ss.setCgpa = cgpa
print("Name : ", ss.getName)
print(f"Semester : {ss.getSemester}")
print(f"Cgpa : {ss.getCgpa}")
