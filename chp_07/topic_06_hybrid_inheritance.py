class A: # PARENT CLASS OF B AND C
    def func1(self):
        print("This is class A method")
class B(A): # PARENT CLASS OF D
    def func2(self):
        print("This is class B method")
class C(A): # PARENT CLASS OF D
    def func3(self):
        print("This is class C method")
class D(B,C): # CHILD CLASS OF B AND C
    def func4(self):
        print("This is class D method")
# Creating an object
dd = D()
dd.func1()
dd.func2()
dd.func3()
dd.func4()