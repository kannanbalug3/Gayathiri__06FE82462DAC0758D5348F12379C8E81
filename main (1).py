#1.2 write a program that determines whether a year entered by the user is a leap year or not using ifelif-else statement
year=2023
#to get year (integer input)from the user
#year=int(input('enter a year:"))
#divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if(year%400==0)and (year % 100==0):
   print("{0}is a leap year".format(year))