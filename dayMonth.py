#Write a program that takes day and month from the command line and prints true if day of month is between March 20 and June 20, false otherwise.

from sys import argv
month = argv[1]
day = int(argv[2])

if month == 'march' or month == 'april' or month == 'may' or month == 'june':
    if month == 'march':
        if day >= 20 and day <= 31:
            print(True)
        else:
            print(False)
    elif month == 'april':
        if day >= 1 and day <= 30:
            print(True)
        else:
            print(False)
    elif month == 'may':
        if day >= 1 and day <= 31:
            print(True)
        else:
            print(False)
    elif month == 'june':
        if day >= 1 and day <= 20:
            print(True)
        else:
            print(False)
else:
    print(False)
