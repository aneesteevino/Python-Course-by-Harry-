# dictionary in python

# dictionary is a collection of key-value pairs
# dictionary is mutable(can be changed)
# dictionary is defined by curly brackets
# dictionary is used to store multiple items in a single variable
# dictionary is used to store the data in the form of key-value pairs
# dictionary is unordered

#  real life uses of dictionary
# 1. hum  dictionaries ko as a phone book use krty hain
# 2. hum dictionaries ko as a database use krty hain
# 3. hum dictionaries ko as a configuration file use krty hain
# 4. hum dictionaries ko as a json file use krty hain
# 5. hum dictionaries ko as a data structure use krty hain
# hum dictionaries sy data ko search krty hain
# hum dictionaries sy data ko update krty hain
# hum dictionaries sy data ko delete krty hain
# hum dictionaries sy marksheet bna kr data ko store krty hain



# dictionary={"name":"Anees","age":18,"study":"Ai","city":"Karachi"}
# dic={32:"Anees",33:"salahuddin",34:"sahil"}
# print(dic[32]) # it will print the value of the key 32
# print(dictionary["name"]) 

# dic={"name":"Anees","age":18,"study":"Ai","city":"Karachi"}
# print(dic["name"]) # it will print the value of the key name if it is present in the dictionary
# print(dic[name2]) # it will give an error because the key name2 is not present in the dictionary
# print(dic.get("name")) # it will print the value of the key name if it is present in the dictionary
# print(dic.get("name2")) # it will print none because the key name2 is not present in the dictionary

# to access all the keys of the dictionary we use the keys() method
# dic={"name":"Anees","age":18,"study":"Ai","city":"Karachi"}
# print(dic.keys()) # it will print all the keys of the dictionary
# print(dic.values()) # it will print all the values of the dictionary
# for i in dic.keys():
#     print(i) # it will print all the keys of the dictionary

# for i in dic.values():
#     print(i) # it will print all the values of the dictionary

# # accessing key values by f string in for loop
# dic={"name":"Anees","age":18,"study":"Ai","city":"Karachi"}
# for i in dic:
#     print(f"the key is {i} and the value is {dic[i]}") # it will print the key and the value of the dictionary

# print(dic.items()) # it will print the key value pairs of the dictionary

# dic  = {"name":"Anees","age":18,"study":"Ai","city":"Karachi"}
# for key,value in dic.items():
#     print(f"the key is {key} and the value is {value}") # it will print the key and the value of the dictionary



# dictionary methods in python

# 1. clear() method ( it will clear the dictionary)
# example
# dic  = {"name":"Anees","age":18,"study":"Ai","city":"Karachi"}
# dic.clear()
# print(dic) # it will clear the dictionary

# 2. copy() method ( it will copy the dictionary)
# example
# dic  = {"name":"Anees","age":18,"study":"Ai","city":"Karachi"}
# dic1=dic.copy()
# print(dic1) # it will copy the dictionary

#3. update() method ( it will update the dictionary)
# example
# dic  = {"name":"Anees","age":18,"study":"Ai","city":"Karachi"}
# dic.update({"name":"Ali","age":20})
# print(dic) # it will update the dictionary


# 4. pop() method ( it will remove the element from the dictionary)
# example
# dic  = {"name":"Anees","age":18,"study":"Ai","city":"Karachi"}
# dic.pop("name")
# print(dic) # it will remove the element from the dictionary


# clear() method ( it will clear the dictionary)
# example
# dic  = {"name":"Anees","age":18,"study":"Ai","city":"Karachi"}
# dic.clear()
# print(dic) # it will clear the dictionary

# 5 popitem() method ( it will remove the last element from the dictionary)
# example
# dic  = {"name":"Anees","age":18,"study":"Ai","city":"Karachi"}
# dic.popitem()
# print(dic) # it will remove the last element from the dictionary


# 6. del keyword ( it will delete the dictionary)
# example
# dic  = {"name":"Anees","age":18,"study":"Ai","city":"Karachi"}
# del dic["age"] # it will delete the key age from the dictionary
# del dic # it will delete the dictionary
# print(dic) # it will give an error because the dictionary is deleted



# for loops in dictionary
# dic  = {"name":"Anees","age":18,"study":"Ai","city":"Karachi"}
# values=dic.items()
# for i in  values:
#     print(i) # it will print the keys of the dictionary

# my_dict={
#     'name':"Abdul samad",
#     'age':20,
#     'RollNo':"23bsai015",
#     'Occupation':"Ai Enginner"
# }
# my_dict['Occupation']="Student"
# print(my_dict)

# deleting 



# adding new key value pair
# my_dict={
#     'name':"Abdul samad",
#     'age':20,
#     'RollNo':"23bsai015",
#     'Occupation':"Ai Enginner"
# }
# my_dict['city']="Karachi"
# print(my_dict)


#  mini real world project on  dictionary

# 1. hum dictionaries ko as a phone book use krty hain


# phone_book = {
#     "Anees": 123456,
#     "Ali": 123456,
#     "Ahmed": 123456,
#     "Salahuddin": 123456,
#     "Sahil": 123456
# }

# def print_menu():
#     print("Welcome to the phone book")
#     print("1. Add a contact")
#     print("2. Search a contact")
#     print("3. Delete a contact")
#     print("4. Update a contact")
#     print("5. Show all contacts")
#     print("6. Exit")
    

# def add_contact():
#     name = input("Enter the name: ")
#     try:
#         number = int(input("Enter the number: "))
#         phone_book[name] = number
#         print("Contact added successfully")
#     except ValueError:
#         print("Invalid number. Please enter a valid integer.")

# def search_contact():
#     name = input("Enter the name: ")
#     if name in phone_book:
#         print(f"The number of {name} is {phone_book[name]}")
#     else:
#         print("Contact not found")

# def delete_contact():
#     name = input("Enter the name: ")
#     if name in phone_book:
#         del phone_book[name]
#         print("Contact deleted successfully")
#     else:
#         print("Contact not found")

# def update_contact():
#     name = input("Enter the name: ")
#     if name in phone_book:
#         try:
#             number = int(input("Enter the number: "))
#             phone_book[name] = number
#             print("Contact updated successfully")
#         except ValueError:
#             print("Invalid number. Please enter a valid integer.")
#     else:
#         print("Contact not found")

# def show_all_contacts():
#     for name, number in phone_book.items():
#         print(f"The number of {name} is {number}")

# def main():
#     while True:
#         print_menu()
#         try:
#             choice = int(input("Enter your choice: "))
#             if choice == 1:
#                 add_contact()
#             elif choice == 2:
#                 search_contact()
#             elif choice == 3:
#                 delete_contact()
#             elif choice == 4:
#                 update_contact()
#             elif choice == 5:
#                 show_all_contacts()
#             elif choice == 6:
#                 break
#             else:
#                 print("Invalid choice")
#         except ValueError:
#             print("Invalid input. Please enter a number between 1 and 6.")

# if __name__ == "__main__":
#     main()
