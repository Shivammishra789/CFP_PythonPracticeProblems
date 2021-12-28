#Use random function to get single digit
import random
num = int(random.random()*10)
print(num)

#Use Random to get Dice Number between 1 to 6
randomDice1 = random.randint(1,6)
print(randomDice1)

#Add two random dice number and print the result
randomDice2 = random.randint(1,6)
print(randomDice2)
print('The sum of 2 random dice is: ',randomDice1 + randomDice2)

#Write a program that reads 5 Random 2 Digit values , then find their
#sum and the average
sumOfDice= 0
for i in range(0,6):
    randomDice = random.randint(10,100)
    print(randomDice)
    sumOfDice += randomDice
print(sumOfDice)
