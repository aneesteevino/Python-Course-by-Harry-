# tuple in python

# tuple is a collection of items in a particular order
# tuples are immutable(can not be changed)
# tuples are defined by round brackets
# tuples are used to store multiple items in a single variable

# tuple1=(1,2,3,4,5,"Anees",6,7,8,9,10)
# print(tuple1) # it will print the whole tuple

# to make tuple of one element you need to put comma after elemnet
# tuple=(1)
# print(type(tuple), tuple) # if u put only one element in the tuple without comma it will consider it as an integer
# tuple=(1,)
# print(type(tuple), tuple) # if u put only one element in the tuple with comma it will consider it as a tuple

# tuple=(1,2,4,5,65,8,"anees","ali ,")
# print(tuple[1])
# print(tuple[1:5])

#  it is also an example of tuple
# tuple=1,
# print(type(tuple), tuple)

# if "anees" in tuple:
#     print("g bhai isme hai ye  nam")
# else :
#     print("nahi hai ye nam")  

# print(tuple[1:3])

# tuple methods in python

# tuple methods are used to manipulate the tuples
# tuple methods are used to perform different operations on tuples
# here are some tuple methods
# 1. count() method ( ye method tuple mai koi bhi element kitni dafa hai wo count krta hai )
# 2. index() method ( ye method tuple mai koi bhi element ka index return krta hai )

# count method

# tuple=(1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10)
# tuple1=tuple.count(1)
# print(tuple1)


# index method

# tuple=(1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10)
# tuple1=tuple[4]
# print(tuple1) # ye method kisi bhi element ki index btata hai

# tuple mai changing krny k liye apko tuple ko list mai convert krna hoga 
#phir usko change kr k phir se tuple mai convert krna hoga


# countries=("pakistan","india","china","usa","uk")
# countries=list(countries)
# countries[1]="australia"
# countries=tuple(countries)
# print(countries)
# print(type(countries))


# concatenating two tuples
# tuple1=(1,2,3,4,5)
# tuple2=("a","b","c","d","e")
# k=tuple1+tuple2
# print(k)


# tuple=("Anees",1,2,3,4,5)
# # tuple1= tuple.index("Anees")
# # tuple1= tuple.index(2) # it will give the index of the element 2 any element covered with index will give the index of the element

# print(len(tuple)) # it will give the length of the tuple


# accessing elements of tuple through negative indexing

# tuple=("Anees",1,2,3,4,5)
# print(tuple[-1]) # it will give the last element of the tuple

# tuple = ("Anees", 1, 2, 3, 4, 5,["anees","ali","ahmed"]) it is updating the list in the tuple
# tuple[6][1]="khan"
# print(tuple)

# nested indexing in tuple

# tuple = ("Anees", 1, 2, 3, 4, 5,["anees","ali","ahmed"])
# print(tuple[6][1]) # it will give the element of the list which is in the tuple


# slicing operation in tuple

tuple = ("Anees", 1, 2, 3, 4, 5,["anees","ali","ahmed"])
# print(tuple[1:5]) # it will give the elements from index 1 to 4
# print(tuple[1:5:2]) # it will give the elements from index 1 to 4 with a step of 2
# print(tuple[1:5:3]) # it will give the elements from index 1 to 4 with a step of 3
# print(tuple[::-1]) # it will reverse the tuple
# print(tuple[::-2]) # it will reverse the tuple with a step of 2
# print(tuple[:]) # it will give the whole tuple 
# print(tuple[::]) # it will give the whole tuple

# you can not directly change the element of the tuple but you can change the element of the list which is in the tuple


# nested tuple

# tuple = ("Anees", 1, 2, 3, 4, 5,("anees","ali","ahmed"))


