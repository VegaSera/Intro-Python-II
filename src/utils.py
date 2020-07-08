import random

def dice(num, sides, mod):
    total = 0
    for i in range(num):
        total += random.randint(1, sides)
    return total+mod