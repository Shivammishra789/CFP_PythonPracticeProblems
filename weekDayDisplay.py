# Read a Number and Display the week day (Sunday, Monday,...)
dayNumber = int(input('Enter number to display week day: '))
print(dayNumber)
if dayNumber == 1:
    print('Sunday')
elif dayNumber == 2:
    print('Monday')
elif dayNumber == 3:
    print('Tuesday')
elif dayNumber == 4:
    print('Wednesday')
elif dayNumber == 5:
    print('Thursday')
elif dayNumber == 6:
    print('Friday')
elif dayNumber == 7:
    print('Saturday')
else:
    print('enter valid input')
