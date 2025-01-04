# Exception handling in python

# in  python we can explicitly handle errors and we can print our own user friendly message instead of system generated error  message
#   exception handling is used to handle the exceptions
# exception handling is used to handle the errors
# exception handling is used to handle the runtime errors
# exception handling is used to handle the logical errors
# exception handling helps to avoid the program to crash




# example: 1 
# try:
#   num=int(input("enter a number  :"))
#   for i in range(1,11):
#     print(num,"x",int(i),"  =  ",int(num*i))
# except :
#        print("sorry yr tumny number ji jgah nam likhdia")
    

# Example : 2
# try :
#     num=int(input("enter a number : "))
#     l=[2,3]
#     print(l[num])
# except ValueError:
#     print("you entered string instead of integer ")
# except IndexError:
#      print("you entered invalid index ")

# finally clause
# we write some statements that would always be executed after using finally keyword 
 
# def func1():
#   try:
#     a=int(input("enter a index :  "))
#     l=[1,2,3,4,5]
#     print(l[a])
#     return 1
#   except IndexError:
#     print("index not found !!!")
#     return 0
#   finally:
#      print("mai to hamesha execute honga")

# print("finally ki trah mai bhi to hamesha execute kr rha hun to finally kyun use kr rhy ho ?  ")
# x=func1()
# print(x)



# Raising custom errors
#  in python we can raise custom errors by using raise keyword

# num=int(input("enter a number b/w 5 and 10 : "))
# if (5<num>10 or num>10 or num<5):
#     raise ValueError("value should be between 5 and 10 ")


#  difference b/w raising custom error and exception handling

# exception handling is used to handle the errors
# exception handling is used to handle the runtime errors
# exception handling is used to handle the logical errors

# raising custom error is used to raise the custom errors
# raising custom error is used to raise the user defined errors
# raising custom error is used to raise the errors that are not handled by the system
# raising custom error is used to raise the errors that are not handled by the user



# a=input("write quit : ")
# if a=="quit":
#     print(a)
# else:
#     raise ValueError("you've enntered invalid input")
