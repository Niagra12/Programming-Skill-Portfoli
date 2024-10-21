
"""
Exercise 10: Is it even? - 35 Marks
***********************************
"""

#function checking if the number is even or odd.
def even_or_odd(number):
    if number % 2 == 0:
        return f"{number} is an even number."
    else:
        return f"{number} is an odd number."
#main function to handle the user input and the print result.
def main():
    number = int(input("Enter a number: "))
    result = even_or_odd(number)
    print(result)
#entry point of the program
if __name__ == "__main__":
    main()

