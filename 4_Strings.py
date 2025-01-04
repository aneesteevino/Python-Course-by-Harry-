# string in python

#  any thing in single quotes or double quotes is a string in python
# string is a collection of characters  
# string is immutable (can not be changed)
# string is defined by single quotes or double quotes
# string is a sequence of characters

# a="hi"
# b="bye"
# c="hi"

# # print(a,b,c)

# a="2"
# print(a*3) # here it will print the string 3 times


# print('''he said "iam at home''') 
# print('''he said \'iam at home\'''') 



# indexing of string in python


# string="Anees"
# print(string[0]) # it will print the first character of the string



#indexing 

# naame="Anees"


# print(naame[1])

# print(naame[1])

# print(naame[2])

# print(naame[1])

# print(naame[1])

# print(naame[1])


# for loop in string

# name="Anees" # here we are defining a string
# for i in name: # here we are using for loop to print the string
#     print(i)

# # slicing of string in python

# # slicing is a process of extracting a part of string 
# # slicing is done by using colon
# # slicing is done by using square brackets
# # slicing is done by using index


# names="MUHAMMAD , ANEES"
# # # to know the length of string we use len function 
# print(len(names)) 
# # # to know the last character of string we use -1 index
# print(names[-1])
# print(names[-2])
# print(names[-3])
# print(names[-4])
# print(names[-5])


# fruit="watermelon"
# length=len(fruit)
# print("lenght of word ",fruit , "is : ",length)

# slicing of string
# print(fruit[1:1]) # it will not print any thing because the starting and ending index is same
#print(fruit[0:2]) # it will print the first two characters of the string 
# print(fruit[2:3]) # it will print the third character of the string
#print(fruit[:5]) # here python will take the starting index as 0
# print(fruit[:]) # if u dont put anny index python will automatically display the whole string
# print(fruit[:0]) # it will not print any thing because the starting and ending index is same
# print(fruit[0:]) # it will print the whole string
# print(fruit[-1:-3]) # it will not print any thing because the starting index is greater than the ending index
#print(fruit[-3:-1]) # it will print the 2ndlast two characters of the string
#print(fruit[-3:4]) # not logically valid because you can not start any index by  any negeative index
#print(fruit[5:2])# it will not print any thing because starting iindex should not be greater than ending index
# print(fruit[6:7], fruit.index("m"))  # it will print the 7th character of the string
#

# string methods in python

# string methods are used to manipulate the strings
# string methods are used to perform different operations on strings
# here are some string methods
# 1. upper() method
# 2. lower() method is used to convert the string into lower case
# 3. title() method
# 4. capitalize() method
# 5. swapcase() method
# 6. count() method
# 7. find() method
# 8. index() method
# 9. replace() method
# 10. split() method is used to split the string by the given character and return a list
# 11. join() method
# 12. strip() method is used to remove any white spaces from the string
# 13. lstrip() method
# 14. rstrip() method  this method is used to remove any  white spaces from the right side of the string
# 15. isdigit() method
# 16. isalpha() method
# 17. isalnum() method
# 18. isspace() method
# 19. startswith() method
# 20. endswith() method
# 21. center() method
# 22. ljust() method is 
# 23. rjust() method
# 24. format() method
# 25. encode() method
# 26. decode() method
# 27. isupper() method
# 28. islower() method
# 29. istitle() method
# 30. isidentifier() method


# strings are immmutable 
name="Anees"
# print(name.upper() ) # it will convert the string into upper case but it will not change the original string
# print(name.count("A")) # it will count the number of times the character is repeated in the string
# print(name.rstrip("a")) # it will remove the right side white spaces from the string
# print(name.endswith("s")) # it will check the last character of the string and return true or false
# print(name.replace("A","a")) # it will replace the character in the string
# print(name.split("n")) # it will split(means to break from) the string by the given character and return a list

#print(name.capitalize()) # it will capitalize the first character of the string and convert the rest of the characters into lower case
# print(name.center(50)) # it will center the string in the given width and fill the remaining space with white spaces
# print(name.find("e")) # it will find the index of the given character in the string of the first occurance
# print(name.index("e")) # it will find the index of the given character in the string of the first occurance
