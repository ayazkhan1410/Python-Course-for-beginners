class Parent1: # object is super class of parent
    def __init__(self):
        super().__init__()
        print("This is Father class Constructor ....")
    def father(self):
        print("This is father class method")
class Parent2:
    def __init__(self):
        super().__init__()
        print("This is Mother class Constructor ....")
    def mother(self):
        print("This is mother class method")
class Child(Parent1,Parent2):
    def __init__(self):
        super().__init__()
        print("This is child class Constructor ....")
    def son(self):
        print("This is child class method")
# creating an object
cc = Child()
cc.father()
cc.mother()
cc.son()

# Another Example
# class BackendDev:
#     lang_names = 'Java & Oracle'
#     def backend_work(self):
#         print(f"implementing backend work with : {self.lang_names}")
# class FrontendDev:
#     lang_names2 = 'HTML,CSS & JAVASCRIPT '
#     def front_work(self):
#         print(f"implementing frontend work with : {self.lang_names2}")
# class TeamLead(BackendDev,FrontendDev):
#     def website_created(self):
#         print("Website created sucessfully ...")
# # creating an object
# tt = TeamLead()
# tt.backend_work()
# tt.front_work()
# tt.website_created()



