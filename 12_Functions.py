# functions in python

#Functions in programming help avoid repeating code by
# separating logic into reusable entities,
# reducing errors and code length. Functions make code modular and easier to maintain and update.

# def greet():
#     print("hello world")    
# greet() # here we are calling the function greet


# def CalculateGmean(a,b):
#     gmean=(a*b)/(a+b)
#     a=25
#     b=40
#     if(a>b):
#         print("a is greater than b")
#     else:
#         print("b is greater than a")
#     print("the Geometric mean of a and b is : ",gmean) 
#     c=int(input("enter 1st number : "))
#     d=int(input("enter 1st number : "))
#     if(c>d):
#         print("1st is greater than 2nd number")
#     else:
#         print("2nd number is greater than 1st number")
#     gmean1=(c*d)/(c+d)
#     print("the Geometric mean of c and d is : ",gmean) 

# CalculateGmean(25,40) # here we are calling the function CalculateGmean

# def isGreater(a,b):
#     pass # yahan pr ap is function ko as a dummy function rkha hua hai abhi tk mtlb ap isme bad mai aaky kuch functionality add karein gy


# types of functions in python

# 1. built-in functions (wo functions jinko humei def keyword k baghair use krna hota hai)
# 2. user-defined functions (wo functions jo humei def keyword k sath define krna hota hai)

# built-in functions in python

# built-in functions are the functions that are already defined in python
#example min(), max(), sum(), len(), print(), input(), type(), id(), abs(), round(), pow(), sorted(), reversed(), range(), zip(), enumerate(), all(), any(), filter(), map(), reduce(), open(), close(), write(), read(), append(), seek(), tell(), flush(), split(), join(), strip(), lstrip(), rstrip(), isdigit(), isalpha(), isalnum(), isspace(), startswith(), endswith(), center(), ljust(), rjust(), format(), encode(), decode(), isupper(), islower(), istitle(), isidentifier(), upper(), lower(), title(), capitalize(), swapcase(), count(), find(), index(), replace(), split(), join(), strip(), lstrip(), rstrip(), isdigit(), isalpha(), isalnum(), isspace(), startswith(), endswith(), center(), ljust(), rjust(), format(), encode(), decode(), isupper(), islower(), istitle(), isidentifier(), upper(), lower(), title(), capitalize(), swapcase(), count(), find(), index(), replace(), split(), join(), strip(), lstrip(), rstrip(), isdigit(), isalpha(), isalnum(), isspace(), startswith(), endswith(), center(), ljust(), rjust(), format(), encode(), decode(), isupper(), islower(), istitle(), isidentifier(), upper(), lower(), title(), capitalize(), swapcase(), count(), find(), index(), replace(), split(), join(), strip(), lstrip(), rstrip(), isdigit(), isalpha(), isalnum(), isspace(), startswith(), endswith(), center(), ljust(), rjust(), format(), encode(), decode(), isupper(), islower(), istitle(), isidentifier(), upper(), lower(), title(), capitalize(), swapcase(), count(), find(), index(), replace(), split(), join(), strip(), lstrip(), rstrip(), isdigit(), isalpha(), isalnum(), isspace(), startswith(), endswith(), center(), ljust(), rjust(), format(), encode(), decode(), isupper(), islower(), istitle(), isidentifier(), upper(), lower(), title(), capitalize(), swapcase(), count(), find(), index(), replace(), split(), join(), strip(), lstrip(), rstrip(), isdigit(), isalpha(), isalnum(), isspace(), startswith(), endswith(), center(), ljust(), rjust(), format(), encode(), decode(), isupper(), islower(), istitle(), isidentifier(), upper(), lower(), title(), capitalize(), swapcase(), count(),

# user-defined functions in python
# user-defined functions are the functions that are defined by the user
# user-defined functions are defined by using def keyword
# user-defined functions are used to avoid repeating code

# def greet():
#     print("hello world")
# greet() # here we are calling the function greet and its a user-defined function


# function arguments in python

# function arguments are the values that are passed to the function
# there are 4 types of function arguments
# 1. default arguments
# 2. keyword arguments
# 3.variable-length arguments
# required arguments

# default arguments in python

# default arguments are the arguments that have a default value
# if the user does not pass the value to the function then the default value will be used
# default arguments are defined by using the assignment operator
# default arguments are defined at the end of the function
# def average(a,b): # here a and b are the arguments of the function average
#  print("the average of ", a, "and ",b , "is : " ,(a+b)/2)
# average(10,20) # here we are passing the values 10 and 20 to the function average


# # example 
# def average(a=19,b=80): # here a and b are the default arguments of the function average
#  print("the average of ", a, "and ",b , "is : " ,(a+b)/2)
# average()# average(12,45) agr ap ider iss bracket mai koi value dengy a or b ki to wo uper waly given values ko ignore krdega or apki  iss bracket mai di hui values ko consider karega
#          # or agr ap koi value nhi dengy to wo default values ko consider karega jo k uper di hui hain 
#          #average(10) sirf a ki value di hui hai or b ki value nhi di hui hai to b ki value default value ko consider karega



# def name (fname , mname = "Anees", lname =  "Teevino"):
#       print("hi ", fname , mname , lname)
# name("MUHAMMAD ")


# keyword arguments in python

# keyword arguments are the arguments that are passed to the function by using the keyword
# def name (fname , mname = "Anees", lname =  "Teevino"):
#       print("hi ", fname , mname , lname)
# name("hello  ","extra ","words") # here we are passing the values to the function name by using the keyword



# required arguments in python
# required arguments wo  arguments hain jo k function mai hona zaroori hoty hain
# example
# def num( a=7 , b=8) :# here a and b are the required arguments of the function num jo k humein lazmi deny hain inky values agr nhi dengy to error ayeg
#     print("the numbers are  : " ,a,b)
# num(a=2,b=4) #

# # example 
# def num(a,b,c=10):
#     print("the sum is ",a+b+c)
# num(45,4)# here we are only providing the values of a and b and not providing the value of c so it will take the default value of c


# 3.variable-length arguments
# wo arguments hain jo k function mai jitny bhi arguments hain wo accept kr lety hain

# def average(*num): # its taking arguments in the form of tuple
#     #print(type(num)) 
#     sum=0
#     for i in num:
#         sum=sum+i
#     print("the average is : ",sum/len(num))
# # average(2,4) # here we are passing the values to the function average
# average(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15) # here we are passing the values to the function average


# def info(**information): # its taking arguments in the form of dictionary
#      print("hi ",  information["fname"], information ["mname"], information ["lname"])

# info(fname="Anees", mname="Muhammad", lname="Teevino") # here we are passing the values to the function info by using the keyword


# return statement in python

# return statement is used to return the value from the function
# return statement is used to exit the function

# def average(*num): # its taking arguments in the form of tuple
#     #print(type(num))
#     sum=0
#     for i in num:
#         sum=sum+i
#         return 7 # it will return the value 7 and exit the function 
#     # jo pehli return value milegi usko run  kr k baqi koi bhi return value nhi chalay ga
#     return sum/len(num)
# a=average(2,4)
# print(a)


#  Enumerate function
# enumerate function wo function hai jo k humein index or value dono return krta hai
# enumerate function mai hum kisi bhi (list,tuple,set,dictionary) k elements ko access kr skty hain
# instead of using the range function we use the enumerate function
# enumerate function is used to iterate over the sequence

# l=[1,2,3,4,5,6,7,8,9,10]
# for index,value in enumerate(l):
#     print(value)
#     if index==2:
#        print("you are on index 2 ") # it will print the index and value of the list

# tuple=("mango","banana","apple","gava")
# for index,fruits in enumerate(tuple):
#     print(index,fruits)

dic={"name":"anees","caste":"teevino"}
for index,dictionary in enumerate(dic):
    print(index,dic)


# recursion in python

# recursion is a process in which a function calls itself
# n=int(input("enter a number : "))
# def factorial(n):

#     if(n==0 or n==1):
#         return 1
#     else :
#         return n*factorial(n-1)  # hity asaan 

# print(factorial(n)) # it will print the factorial of the number 5 


# fibonacci series in python

# formula of fibonacci series is
# fibonacci(n)=fibonacci(n-1)+fibonacci(n-2)

# print fibonacci series using recursion


# for nth number in fibonacci series
# n=int(input("enter a number : "))
# def fibonacci(n):
#     if  n== 0 or n==1 :
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(n)) # 
