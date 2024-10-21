
"""
Exercise 3: Biography - 25 Marks
********************************
"""

name = input("Enter your full name: ")
hometown = input("Enter your hometown: ")

while True:
    age = (input("Enter your age: "))

    try:
        age = int(age)
        break
    except ValueError:
        print("Please enter a valid age (a number)")
print(f"Name: {name}\nHometown: {hometown}\nAge: {age}")


"""
It starts by asking the user's  name, hometown, and age as strings. 
The age uses while loop with a try and except block to constantly ask the user for the input-
until the user provides a valid integer.
If the input for the age isn't a valid number or an integer, it will print an error message-
("Please enter a valid age (a number)" and prompts the user again.
Once a valid age/integer is given, it will exit the loop and print all the information.
"""
