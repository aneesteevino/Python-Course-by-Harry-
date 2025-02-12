#                                    ****sets in python**** 

# sets are the collection of unordered items 
# sets are defined by curly brackets
# sets are mutable(can be changed)
# sets are used to store multiple items in a single variable
# sets do not allow duplicate items
# sets are used to perform different operations like union, intersection, difference, symmetric difference, subset, superset, disjoint

# set1={1,2,3,4,5,6,7,8,9,10}
# print(set1) # it will print the whole set

# set1={1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10}
# print(set1) # it will not print the duplicate values

# set1={1,2,3,4,5,6,7,8,9,10}
# print(1 in set1) # it will check if the element is present in the set or not

# set1={1,2,3,4,5,6,7,8,9,10}
# set1.add(11) # it will add the element to the set


# set1={1,2,3,4,5,6,7,8,9,10}
# set1.update([11,12,13,14,15]) # it will add the elements to the set
# print(set1)
#                    OR 
# s1={1,2,3}
# s2={4,5,6}
# s1.update(s2) # it will add the elements of s2 to s1
# print(s1)

# symetric difference = (A-B) U (B-A) iska hai jo common elements hain unko chor k baqi elements ko print krta hai
# A={1,2,3,4,5,6,7,8,9,10}
# B={5,6,7,8,9,10,11,12,13,14}
# print(A.symmetric_difference(B)) # it will print the symmetric difference of the two sets


#difference 
# A={1,2,3,4,5,6,7,8,9,10}
# B={5,6,7,8,9,10,11,12,13,14}
# # print(A.difference(B)) # isme wo elements print hongy jo A mai hain or B mai nhi hain
# #                OR 
# print(A.difference_update(B)) # isme wo elements print hongy jo A mai hain or B mai nhi hain 



# set1={1,2,3,4,5,6,7,8,9,10}
# set1.remove(10)

# print(set1) # it will remove the element from the set

# set1={1,2,3,4,5,6,7,8,9,10}
# set1.discard(10) # it will remove the element from the set

# set1={1,2,3,4,5,6,7,8,9,10}
# set1.pop() # it will remove the last element from the set

# set1={1,2,3,4,5,6,7,8,9,10}
# set1.clear() # it will clear the set

# set1={1,2,3,4,5,6,7,8,9,10}
# s2={11,12,13,14,15,16,17,18,19,20}
# print(set1.union(s2)) # it will return the union of the two sets
# it will add the elements to the set

# set1={1,2,3,4,5,6,7,8,9,10}
# s2={11,12,13,14,15,16,17,18,19,20}
# print(set1.intersection(s2)) # here nothing is common in the two sets so it will return an empty set



# s1={1,2,3}
# s2={1,2,3,4,5,6,7,8,9,10}
# print(s1.intersection(s2)) # it will return the common elements of the two sets
# # print(s1.intersection_update(s2)) # it will return the none value because it will update the s1 set with the common elements of the two sets and will not print the common elements
# # to do so we use the intersection method
# s1.intersection_update(s2)
# print(s1)# now it will print the common elements of the two sets


#  disjoint method mai dekhty hain k agr A set ka koi bhi element B set mai hai to false return karega agr koi bhi element nhi hai to true return karega
# s1={1,2,3}
# s2={7,5,6,7,8,9,10}
# print(s1.isdisjoint(s2)) # it will return the true because there are no common elements in the two sets


# issuperset() iss method mai python dekhege agr B set k sary elements A set mai hai to true return krega wrna false

# a={1,2,3}
# b={1,2}
# print(a.issuperset(b))
# print(b.issubset(a))


#add() method ( it will add only one element to the set)
# set1={1,2,3,4,5,6,7,8,9,10}
# set1.add(11) # it will add the element to the set
# print(set1)

# update() method ( it will add multiple elements to the set)
# s1={"anees","ali","kamran","zain","samad","tayyab"}
# s1.update(["azhar","kabeer","Qalab","siraj"])
# print(s1)

# remove() method ( it will remove the element from the set)
# s1={"anees","ali","kamran","zain","samad","tayyab"}
# s1.remove("anees")# agr ye element set mai nhi hoga to error ayega
# s1.discard("samad")# agr ye element set mai nhi hoga to error nhi ayega
# print(s1)


# pop() method ( it will remove the last element from the set but important thing is that it will remove the random element from the set as the set is unordered)
# s1={"anees","ali","kamran","zain","samad","tayyab"}
# s1.pop()
# print(s1)

# clear() method ( it will clear the set)
# s1={"anees","ali","kamran","zain","samad","tayyab"}
# s1.clear()
# print(s1)


# if and else in sets in python
# a={1,2,3,4,4}
# if 2 in a:
#     print("yes")
# else:
#     print("no")
# del keyword ( it will delete the set) 
# s1={"anees","ali","kamran","zain","samad","tayyab"}
# del s1
# print(s1) # it will give an error because the set is deleted


# anees={"anees","ali","kamran","zain","samad","tayyab",4,5,6,73,2} # it will create a set
# anees={} # it will create a dictionary and this mean empty sets can not be created by using curly brackets
# to  create an empty set we use the set() function
# anees=set() # it will create an empty set
# print(type(anees)) 



# difference between set and tuple
# set is mutable but tuple is immutable
# set is unordered but tuple is ordered
# set is defined by curly brackets but tuple is defined by round brackets
# set does not allow duplicate values but tuple allows duplicate values
# set is used to store multiple items in a single variable but tuple is used to store multiple items in a single variable