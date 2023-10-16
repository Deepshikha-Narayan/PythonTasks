#Create a program that determines whether a given year is a leap year.

year=int(input("Enter year"))
if (year%4==0 and year%100!=0 or year%400==0):
    print("Its a Leap Year")
else:
    print("Its not a Leap Year")