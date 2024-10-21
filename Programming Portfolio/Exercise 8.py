"""
Exercise 8: Simple Search - 30 Marks
************************************
"""



#create the list
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
#
print(names[4])

search_term = input("Enter a name: ")
if search_term in names:
    print(f"{search_term} is in the list")
else:
    print(f"{search_term} is not in the list")