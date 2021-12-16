# Write a program that takes a year as input and outputs the Year is a Leap Year or not
#a Leap Year. A Leap Year checks for 4 Digit Number, Divisible by 4 and not 100 unless
#divisible by 400.

year = int(input('Enter year to check leap year or not '))
if ((year%4) == 0 and (year%100) != 0) or (year%400) == 0:
    print('Its a leap year')
else:
    print('Its not a leap year')
