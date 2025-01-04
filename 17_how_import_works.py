# import  module

# importing in python is process of using  python's prewritten code in our code

# there are 3 ways to import a module in python
# 1. import module
# 2. from module import function_name
# 3. from module import *
# 4. import as (iss sy ap jo module import kr rhy hn uska nam apni mrzi sy rkh skty hain)
# 5. print(dir(math)) iss sy ap dekh skty hain k iss module mai kon kon sy functions hain

# 1. import module
# this is the simplest way to import a module in python
# syntax: import module
# example:
# import math
# ye math ki sari classes or functions ko import krdega jesy k math.sqrt(), math.pi() etc

# example: 1
# import math
# print(math.sqrt(16))
# print(math.pi)


# Example : 2
# import math
# result=math.sqrt(5)
# print(result)



# 2. from module import function_name

# in this way we can import a specific function from a module
# syntax: from module import function_name
# ye sirf us function ko import krega jo ap use krna chahty hain na k sari functions
# example: 1
# from math import sqrt
# print(sqrt(16))

# Example : 2
# from math import sqrt
# result=sqrt(5)
# print(result)


# 3. from module import *
# in this way we can import all the functions and classes from a module
# yhan pr apko . operator use krny ki zaroorat nhi hoti
# syntax: from module import *
# example:
# from math import *
# print(sqrt(16))
# print(pi)


# 4. import as 
# (iss sy ap jo module import kr rhy hn uska nam apni mrzi sy rkh skty hain)

# import math as Anees
# print(Anees.sqrt(3))

# from math import sqrt as square_root

# print(square_root(2))


# 5. dir method
# import pandas
# print(dir(pandas))

# import flask
# print(dir(flask))


# you can create your own module by creating a new file and  then import that file

# exmaple


# from my_module import addtion
# addtion() // ye function meny dusri file mai bnaya hai or mai yhan isko use krskta hun ese hum moi bhi dusri files or  unke functions ko import krwaskte hn

# while buliting your own module you can not directly access any function or variable using (as) methd 
# example: 

# from my_module import addtion as add  // yhan app access krskty hn
# add()


# import my_module as mera_module
# addition()// yhan iss tareky sy app access nhi krskty apko module ka  new name or . lga k access kreingy
# mera_module.addtion() ese hojaega 


# if __name__ == "__main__ in python

# import my_module 
# my_module.Anees()  yhan pr ye 2 times functions ko run krega ek my_module wala or ek import wala iss sy bachne k lye hum if __name__ == "__filename__ use krty hn


# import my_module
# my_module.Anees()