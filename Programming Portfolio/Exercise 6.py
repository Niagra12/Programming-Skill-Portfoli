
"""
Exercise 6: Brute Force Attack - 30 Marks
*****************************************
"""


password = "12345" #the user's password
guess = "" #variable to store user's guess
UserAttempts= 5 #the number of allowed attempts
out_of_guess = False #a flag to indicate if the user runs out of attempts

while guess != password and not out_of_guess: #will track the remaining attempts
    if UserAttempts > 0:
        attempts_remaining = UserAttempts
        guess = input(f"Enter password (Attempts remaining {attempts_remaining}): ") #ask the user to enter the password and will display the remaining attempts.
        UserAttempts = UserAttempts - 1 #will decrease the remaining attempts if the user's input is incorrect.
    else:
        out_of_guess = True #sets the flag to true if there are no more attempts remaining.

if out_of_guess:
    print("The password is incorrect, Please try again later") #if the user has run out of attempts it will print this message.
else:
    print("Correct") #if the user's input is correct, it will print this.
    
    