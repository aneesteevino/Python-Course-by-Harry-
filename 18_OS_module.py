# Os module
# os module is used to interact with the operating system.
# os module provides a way of using operating system dependent functionality.
# os module is a built-in module in python.
# it allows you to do many operating system tasks like: read or write files, manipulate paths, create directories, interacting with the file system etc.
import os

# getcwd() method


# getcwd() method is used to get the current working directory of the file.
# it returns the current working directory of the file.
# syntax: os.getcwd()
# it does not take any parameter.

# example
# cwd = os.getcwd()
# print(cwd)


# chdir() method
# chdir() method is used to change the current working directory to the specified path.
# syntax: os.chdir(path)
# it takes one parameter path which is the new working directory path.
# it does not return anything.

# example
# os.chdir('C:/Users/HP/Desktop')
# cwd = os.getcwd()

# print(cwd)

# import os
# open=input("types yes if u want to open youtube : ")
# if open=='yes' or open=="YES":
# # Open YouTube in the default web browser
#  os.system("start https://www.youtube.com/watch?v=dkVYSsL90Oo&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=46")
# else:
#  print("invalid input !!!")


# important methods of os module

# 1. os.name
# os.name is used to get the name of the operating system dependent module imported.