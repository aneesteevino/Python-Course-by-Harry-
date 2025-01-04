# lists in python

#it is a collection of items in a particular order
#lists are mutable(can be changed)
#lists are defined by square brackets
#lists are used to store multiple items in a single variable

# list1=[1,2,3,4,5,"Anees",6,7,8,9,10]
# print(list1) # it will print the whole list
# print(list1[3])
# #print(list1[12]) # it will give an error because the index is out of range
# print(list1[-2]) # it will print the 2nd last element of the list
# print(list1[1:3]) # it will print the elements from index 1 to 3
# print(list1[:3]) # it will print the elements from index 0 to 3
# print(list1[3:]) # it will print the elements from index 3 to the end
# print(list1[-3:]) # it will print the 3rd last element of the list to the end
# print(list1[1:8:2]) # it will print the elements from index 1 to 8 with a gap of 2
# print(list1[::2]) # it will print the elements of the list with a gap of 2
#print(list1[1:9]) # it will print the elements from index 1 to 9
# if 2 in list1:
#     print("han bhai isme hai ") # it will check if the element is present in the list or not
# if "An" in"Anees":
#     print("han bhai hai ye wala bhi ")
# else :
#     print("nahi hai ye wala ")


# list comprehension in python

# list comprehension is used to create a list in a single line
# list comprehension is used to create a list from an existing list
# list comprehension is used to create a list by applying a condition
# list comprehension is used to create a list by applying a function


# list=[i for i in range(4) ] # it will create a list from 0 to 3
# print(list)

# list=[i for i in range(10) if i %2==0 ] # it will create a list of even numbers from 0 to 9 
# print(list)


# list methods in python

# list methods are used to manipulate the lists
# list methods are used to perform different operations on lists
# here are some list methods
# 1. append() method ( ye method list k end mai koi bhi element add krta hai )
# 2. insert() method ( ye method list k kisi bhi index pr element add krta hai )
# 3. extend() method ( ye method ek list ko dosri list mai add krta hai )
# 4. remove() method ( ye method list mai se koi bhi element remove krta hai )
# 5. pop() method ( ye method list k last element ko remove krta hai )
# 6. clear() method ( ye method list ko clear krta hai )
# 7. index() method ( ye method list mai koi bhi element ka index return krta hai )
# 8. count() method ( ye method list mai koi bhi element kitni dafa hai wo count krta hai )
# 9. sort() method ( ye method list ko sort krta hai )
# 10. reverse() method ( ye method list ko reverse krta hai )
# 11. check() method ( ye method list mai koi bhi element hai ya nhi wo check krta hai )

# extend()
# list1=[1,2,3,4,5,"Anees",6,7,8,9,10]
# list1.extend(["extended"])
# print(list1)

# append()
# list=["a","b","c","d","e"]
# list.append("f")
# print(list)



# concatenate two lists

# list1=[1,2,3,4,5]
# list2=["a","b","c","d","e"]
# k=list1+list2
# print(k)