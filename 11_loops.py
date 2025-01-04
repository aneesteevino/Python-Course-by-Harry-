# # loops in python

# # loops are used to repeat the code
# # there are two types of loops
# # 1. for loop
# # 2. while loop

# # for loop in python

# # for loop is used to iterate over a sequence
# # for loop is used to repeat a block of code for a fixed number of times
 
# name="Anees "
# for i in name:

#     print(i)

# colors=["red","green","blue","yellow","black"]     
# for color in colors:
#     print(color)
#     for i in color:
#         print(i)


# for num in range(1,11): 
#     print(num )


# for num in range(1,12,3): # idher 3rd parameter hum islye pass kr rhy hain k hr ek element k bad 3 ka gap ho
#     print(num )

 
# for num in range(1,11,4): 
#     print(num )

#printing table of 3

# num=3
# for num  in range(1,11):
#     print(num," x ",int(3), " = ",int(num*3))



# # while loop in python

# # while loop is used to repeat a block of code as long as the condition is true

# syntax of while loop
# while condition:
#     block of code

# num=1
# while num<=10:
#     print(num)
#     num=num+1

# num=0
# while num<10:
#    num=int(input("enter a number <10 : "))
#    if num>10:
#     print("no its greater than 10 ")
#    else:
#      print("you entered : ",num ,"and its  less than 10")
# num+=1

# a=0
# while a<=10:
#  a=int(input("enter a number : "))
  
   # it will continue to take input until the user enters a number greater than 10
 
# decrementing while loop

# num=10
# while num>=1:   
#     print(num)
#     num-=1 # it will print the numbers from 10 to 1 in descending order

    # else statement with while loop
# num=10
# while num>=1:
#         print(num)
#         num-=1
# else:
#         print("loop is completed") # it will print the numbers from 10 to 1 in descending order and then print the message that loop is completed

# do while loop in python

# do while loop is not available in python

# emulating do while loop in python
# to create a do while loop in python you need to modify the while loop a little bit
# in order to make it work like a do while loop
# the most common way to do this is to use a while True loop and then use a break statement to exit the loop

# num=0
# while num<=15:
#     print(num)
#     num+=1


# break and continue statement in python

# break statement is used to exit the loop
# continue statement is used to skip the current iteration and continue with the next iteration


# for num in range(1,11) :
#     print(num , " x ", int(10)," = " , num*10)
#     if num==2:
#      break


# for i in range(1,15):
#     if(i==11):
#         break
#     print(i , " X", int(10), " = ", i*10)




# for i in range(1,15):
#     if(i==11):
#         print("skiped 11th iteration")
#         continue
#     print(i , " X", int(10), " = ", i*10)
#     if i==10:
#         break


# for i in [1,2,3,4,5,6,7,8,9,10]:
#     if  i % 2 != 0 :
#         continue
#     print(i) 

 
# break and continue statements in while loop
#Explanation of 'Break Statements' and 'Continue Statements' in Python loops.
# 'Break Statements' exit the loop, 
#'Continue Statements' skip the current iteration, enhancing loop control and efficiency




#Emulating 'Do While Loop' using an 'Infinite While Loop'. 'Do While Loop' executes at least once,
# then based on condition.

# num=1
# while num<=10:
#     print(num)
#     num=num+1
#     if num>=6:
#         break


# i=0
# while i<=11:
#     i=i+1
#     if i==5:
#         continue   
#     print(i)
#     if i==10:
#         break
   
