#Buit-in function
# print("HELLO WORLD")
# result = "This is"
# print(len(result))
# x = round(54.23423452352,1)
# print(x)
# num = -24
# print(abs(num))

# user-defined functions
# def func():
#     print("THIS IS MY FIRST FUNCTION")
# # calling a function
# func()

# def square(number,number2): #5
#     print("Square : ", number*number2)
# number2 = 4
# user_input = int(input("Enter number")) #5
# square(user_input,number2)

# default parameter
# def myfunc(name = "AYAZ",country = "Pakistan"):
#     print(f"my name is {name}, country is : {country}")
# myfunc()
# myfunc("AFFAN","ENGLAND")
# myfunc("ABBAS","UGANDA")

# passing a list
# def func(list1):
#     for item in list1:
#         print(item)
# list1 = ["APPLE",12,True,"AYAZ"]
# func(list1)

# return
# def sum(x,y):
#     return x+y
# result = sum(4,5) #9
# print("SUM : ", result)

# name = "ayaz"
# age = 20
# salary = 2000
# # print("name {1} and age {0}".format(age,name))
# print(f"Name {name}, age{age}, salary {salary}")

# def multiplication(number1,number2):
#     '''
#     this function will take two numbers as an input and
#     multiplay both of numbers
#     '''
#     return number1 * number2
# result = multiplication(5,6)
# print("result : ", result)
# print(multiplication.__doc__)

# recursion
# def fact(number):
#     if number == 0 or number == 1:
#         return 1
#     else:
#         return number * fact(number-1) # 5 * 4 * 3 * 2 * 1
# user_input = int(input("Enter number"))
# result = fact(user_input)
# print("Factorial : ", result)

# def fab(number):
#     if number == 0 or number == 1 or number == 2:
#         return 1
#     else:
#         return fab(number-1) + fab(number-2)
# user_input = int(input("Enter number : "))
# result = fab(user_input)
# print("Fabonaci result : ", result)

#args
# def intelligentstudents(name, *args, **kwargs):
#     print(type(args))
#     print(name)
#     for item in args:
#         print(item)
#     print(type(kwargs))
#     for key,value in kwargs.items():
#         print(f"The value corresenponding to {key} is {value}")
#
# name = "Huraina"
# list1 = ["AYAZ","AFFAN","ABBAS"]
# # intelligentstudents(name, *list1)
# dict1 = {"ALI":23,"LISHO":45,"WANIA":12}
# intelligentstudents(name,list1,**dict1)

from random import choice
import random
# choice
# lucky_number = [1,2,3,4,5,6,7,8,9]
# # print(choice(lucky_number))
# print(f"Lucky number : {choice(lucky_number)}")

#randit
# otp = random.randint(10000,99999)
# print("OTP : ", otp)

# shuffle
# lucky_number = [1,2,3,4,5,6,7,8,9]
# random.shuffle(lucky_number)
# print("Shuffled list : ", lucky_number)

# math modul
# import math
# number = 16
# print(math.sqrt(number))
#
# number2 = 24.324242
# print(math.floor(number2))
# print(math.pow(2,5))

# creating lambda function
# x = lambda a,b : a+b
# y = lambda c,d : c-d
# print(x(5,4))
# print(y(10,5))

# local variable and global variable
var1 = 50
def myfunc():
    global var1
    var1 = 221
    print("Updated value : ", var1)
print("Main method ", var1)
myfunc()
def sum(x,y):
    return x+y
result = sum(5,6)
print(result)
# print(a)
# print(x)
# print(y)