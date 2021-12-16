#Write a program that reads 5 Random 2 Digit values , then find their sum and the average
import random
sum = 0
for num in range(0,5):
    randNum = random.randint(10,99)
    print(randNum)
    sum+=randNum
print('Sum of random 5 two digit numbers is :',sum)
avg = sum/5
print('Average of random 5 two digit numbers is', avg)

'''Unit Conversion

a. 1ft = 12 in then 42 in = ? ft
b. Rectangular Plot of 60 feet x 40 feet in meters
c. Calculate area of 25 such plots in acres'''
feet = 12
inch = 42/feet
print(inch)

rectPlotInFeet = 60*40
print('Rectangular plot in feet is :',"%.2f" % rectPlotInFeet) 
rectPlotInMeter = rectPlotInFeet/(3.281*3.281)
print('Rectangular plot in meters is :',"%.2f" % rectPlotInMeter)

Plots = 25*rectPlotInMeter
PlotsInAcre = Plots/4047
print('Area of plots in acres is: ', "%.2f" % PlotsInAcre)

