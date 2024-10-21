
"""
Exercise 5: Days of the Month - 30 Marks
****************************************
"""


monthConversions = {
    1: "31", #January
    2: "28", #february
    3: "31", #March
    4: "30", #April
    5: "31", #May
    6: "30", #June
    7: "31", #July
    8: "31", #August
    9: "30", #september
    10: "31", #october
    11: "30", #November
    12: "31", #December

}
#a function for leap year
def is_leap_year(year):
    return not (not (year % 4 == 0) or not (year % 100 != 0 or year % 400 == 0))
#ask the user's input for month and year
month = int(input("Enter a month number (1-12): "))
#for february
if month == 2:
    year = int(input("Enter a year: "))
    if is_leap_year(year):
        print(f"February {year} has 29 days")
    else:
        print(f"February {year} has 28 days")
#for other months
else:
     print(f'Month {month} has {monthConversions[month]} days')
#This will print the other months normally


