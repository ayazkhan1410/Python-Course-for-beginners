# try:
# var = int(input("Enter the value of A : "))
# print(var)
# except:
#  print("Value cannot be in String")

# Multiple exception
# try:
#  var1 = int(input("Enter number 1 : "))
#  var2 = int(input("Enter number 2 :"))
#  result = var1/var2
#  print("Division : ", result)
# except ZeroDivisionError:
#  print("Value cannot be divided to 0")
# except Exception as e:
#  print("Exception : ", e)

# Another example
# try:
#  y = 10
#  print(y)
# except NameError:
#  print("Variable not defined")
# except:
#  print("Invalid input")

# Using else
# try:
#  print(y)
#  print("Ayaz Khan")
# except:
#  print("Something went wrong")
# else:
#  print("Thank you for using our program")
# finally:
#  print("Thank you for using our program")

# custom exception class
class MyException(Exception):
 pass
var1 = 21
if var1 > 0:
 raise MyException("Something went wrong")
else:
 print("Valid input")

