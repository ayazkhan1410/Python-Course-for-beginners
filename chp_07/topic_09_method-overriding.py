# class Parent:
#     def disp(self):
#         print("This is Parent class method")
# class Child(Parent):
#     def disp(self):
#         print("This is Child class method")
# # creating an object
# pp = Parent()
# pp.disp()
# cc = Child()
# cc.disp()

# another example
class StateBank:
    def interest(self):
        print("Interest ratio : 7.6")
class AlliedBank(StateBank):
    def interest(self):
        print("Interest ratio : 8.8")
class UBL(StateBank):
    def interest(self):
        print("Interest ratio : 4.5")
# creating an object
ss = StateBank()
ss.interest()

# creating another object
aa = AlliedBank()
aa.interest()

# creating another object
uu = UBL()
uu.interest()