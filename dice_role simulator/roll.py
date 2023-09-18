#env!/usr/bin/env python3
import random

#simulate rolling a six-sided dice
#roll_dice function
def roll_dice(num_rolls):
    results=[]#stores the output after the number of rolls
    for i in range(num_rolls):
        result = random.randint(1, 6)
        results.append(result)
    return result   
num_rolls= int(input("How many rolls do you wanna make: "))
#roll dice and print the result
result = roll_dice(num_rolls)

print("You rolled the dice {} times: {}".format(num_rolls, result))
