'''
An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source

Task

Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

Input Format

Read , the year to test.

Constraints


'''
def is_leap(year):
    leap = False
    if(year%400==0):
        # divisible by 400->leap year
        leap=True
    elif(year%100==0):
        #divisible by 100 but not by 400-> not leap year 
        leap=False
    elif(year%4 ==0):
        #divisible by 4 but not 100
        leap=True       
          
    
        
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))