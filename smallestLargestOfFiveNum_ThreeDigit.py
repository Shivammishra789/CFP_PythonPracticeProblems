#Write a program that reads 5 Random 3 Digit values and then outputs the minimum and the maximum value
import random
randomNumbers = []
for randNum in range(0,5):
    randNum = random.randint(100,999)
    randomNumbers.append(randNum)
print('Random 5 numbers are:',randomNumbers)

if randomNumbers[0] < randomNumbers[1] and randomNumbers[0] < randomNumbers[2] and randomNumbers[0] < randomNumbers[3] and randomNumbers[0] < randomNumbers[4]:
    print('Smallest number is ',randomNumbers[0])
elif randomNumbers[1] < randomNumbers[0] and randomNumbers[1] < randomNumbers[2] and randomNumbers[1] < randomNumbers[3] and randomNumbers[1] < randomNumbers[4]:
    print('Smallest number is ',randomNumbers[1])
elif randomNumbers[2] < randomNumbers[0] and randomNumbers[2] < randomNumbers[1] and randomNumbers[2] < randomNumbers[3] and randomNumbers[2] < randomNumbers[4]:
    print('Smallest number is ',randomNumbers[2])
elif randomNumbers[3] < randomNumbers[0] and randomNumbers[3] < randomNumbers[1] and randomNumbers[3] < randomNumbers[2] and randomNumbers[3] < randomNumbers[4]:
    print('Smallest number is ',randomNumbers[3])
else:
    print('Smallest number is ',randomNumbers[4])


if randomNumbers[0] > randomNumbers[1] and randomNumbers[0] > randomNumbers[2] and randomNumbers[0] > randomNumbers[3] and randomNumbers[0] > randomNumbers[4]:
    print('Largest number is ',randomNumbers[0])
elif randomNumbers[1] > randomNumbers[0] and randomNumbers[1] > randomNumbers[2] and randomNumbers[1] > randomNumbers[3] and randomNumbers[1] > randomNumbers[4]:
    print('Largest number is ',randomNumbers[1])
elif randomNumbers[2] > randomNumbers[0] and randomNumbers[2] > randomNumbers[1] and randomNumbers[2] > randomNumbers[3] and randomNumbers[2] > randomNumbers[4]:
    print('Largest number is ',randomNumbers[2])
elif randomNumbers[3] > randomNumbers[0] and randomNumbers[3] > randomNumbers[1] and randomNumbers[3] > randomNumbers[2] and randomNumbers[3] > randomNumbers[4]:
    print('Largest number is ',randomNumbers[3])
else:
    print('Largest number is ',randomNumbers[4])   

minValue = randomNumbers[0]
for minNum in randomNumbers:
    if minNum < minValue:
        minValue = minNum
print('Minimum value is ',minValue)

maxValue = randomNumbers[0]
for maxNum in randomNumbers:
    if maxNum > maxValue:
        maxValue = maxNum
print('Maximum value is ',maxValue)
