# Write a program to simulate a coin flip and print out "Heads" or "Tails" accordingly.
import random
coinFlip = (random.randint(0,1))
print(coinFlip)
if coinFlip == 0:
    print('Heads')
else:
    print('Tails')
