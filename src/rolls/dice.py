import random

class Die:
    def __init__(self, sides: int):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)
    
class Dice:
    def __init__(self, number: int, sides: int):
        self.number = number
        self.sides = sides
        self.dice_set = [Die(sides) for _ in range(number)]
    
    def roll(self):
        total = 0
        for die in self.dice_set:
            total += die.roll()
        return total
        