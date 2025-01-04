# string formatting in python

# name="Anees"
# study="Ai"
# print("hello world my name is  {} , and i study in {}".format(name,study))

# print("hi my name is {} and i live in {}".format("Anees","Karachi")) # it will print the values in the order they are given
# print("hi my name is {} and i live in {}".format("karachi","ANEES")) # it will print the values in the order they are given to avoid this we use the index
# print("hi my name is {1} and i live in {0}".format("karachi","ANEES")) 


# f string in python

# f string is used to format the string
# f string is used to insert the values in the string
# f string is used to insert the variables in the string
# f string is used to insert the expressions in the string
# we use f string by using the f keyword

# name="Anees"
# age=18
# print(f"hello my name is {name} and my age is {age}") # it will print the values in the string

# name="Anees"
# age=18
# print(f"hello my name is {{name}} and my age is {{age}}") # it will print the values in the string



# price=3.002090838
# txt=f"the price is : {price:.2f}" # it will print the price upto 2 decimal places
# print(txt)



# Doc strings in python
# comment change hoskta hai but doc string nhi hota
# doc strings are used to write the documentation of the function

# def greet():
#     """this function greets the user"""
#     print("hello world")
# greet()
# print(greet.__doc__) # it will print the documentation of the function greet


#difference between doc string and comment
# comment is used to write the comments in the code
 # doc string is used to write the documentation of the function
#  and comment can not be accessed by the user but doc string can be accessed by the user
# doc string is written in triple quotes ''' ''' or """ """


# def square(n): # doc string ko ap def wali line k neeche likhty hain agr ap def wali line k uper likhengy to wo comment hi consider hoga
#                # just def wali line k neeche likhengy to wo doc string consider hoga
#      '''this function returns the square of the number''' 

#      print( n**2)
# square(3)
# print(square.__doc__) # it will print the documentation of the function square
