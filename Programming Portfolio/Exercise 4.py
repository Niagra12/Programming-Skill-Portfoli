

"""
Exercise 4: Primitive Quiz - 30 Marks
*************************************
"""

#created a dictionary consisting of european countries and their capitals.
quiz = {
    "France": "Paris",
    "Spain": "Madrid",
    "Italy": "Rome",
    "Norway": "Oslo",
    "Netherlands": "Amsterdam",
    "Austria": "Vienna",
    "Sweden": "Stockholm",
    "United Kingdom": "London",
    "Portugal": "Lisbon",
    "Germany": "Berlin"
}


score = 0 #set the default score to 0 which will increase by 1 if the answer is correct.
"""
Created a game logic using if function and ignoring the capitals for the user's input.
"""
print("This is the European countries capital guessing game!\n")
playing = input("Do you wanna play the quiz? (yes/no): ").strip().lower()
if playing == "yes":
    print("Okay! Have fun playing the quiz!!")

else:
    print("Run the program again if you want to play.")
    quit() #to end the program if the user's input is "no".


for country, capital in quiz.items():#a loop through each country and ask for their capital

    answer = input(f"What is the capital of {country}? ").strip() #ask user the question.


    if answer.lower() == capital.lower(): #to check if the answer is correct and will ignore the capitalization of the user's answer.
        print("Correct!\n") #will print this if the answer is correct.
        score += 1 #will increase the score by 1.
    else:
        print(f"Wrong answer. The capital of {country} is {capital}.\n") #will print this if the answer is wrong and will also show the correct answer.


print(f"Final score is {score} out of {len(quiz)}.") #will print the final score and used "len" to return the number of characters in a text string.


if score == len(quiz):#check if the score is perfect.
    print("Yeyyy! You got all the answers correct!") #will print this if the score is perfect.
elif score > len(quiz) // 2:
    print("Good job! You know most of the European capitals.") #will print this if score is 6-9.
else:
    print("You might wanna study! Try again after you study.") #will print this if the score is less than 5.
