class Student:
    name = 'AYAZ KHAN' # Public
    _gmailid = 'ayazkhan@gmail.com' # Protected
    __password = '0305' #Private
    # def show(self):
    #     print(self.name)
    #     print(self._gmailid)
    #     print(self.__password)
class DepthDetail(Student):
    blood_group = 'B++'
    def show(self):
        print(self.name)
        print(self._gmailid)
        print(self.blood_group)
        # print(self.__password)
       
dd = DepthDetail()
dd.show()