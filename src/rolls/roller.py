from hiros.hiro_class import AbilityScores, HiroClass
from rolls.dice import Dice, Die

class Roller:
    def __init__(self, *, 
                 character: HiroClass=HiroClass('Hiro', AbilityScores(10,10,10,10,10,10)), 
                 roll_type: str=None, 
                 ability: str=None, 
                 skill: str=None, 
                 logging=False,
                 dice: list=['1d20']):
        """
        Initialize the Roller.

        :param character: The character for which the roll is being made
        :type character: HiroClass
        :param roll_type: The type of roll being made
        :type roll_type: str
        :param ability: The ability being rolled for
        :type ability: str
        :param skill: The skill being rolled for
        :type skill: str
        :param dice: The dice being rolled
        :type dice: list
        :param logging: Whether or not to log the roll
        :type logging: bool
        """
        self.character = character
        self.roll_type = roll_type
        self.ability = ability
        self.skill = skill
        self.logging = logging
        self.roll_mod = self.calc_mod()
        self.dice = dice
    
    def calc_mod(self):
        roll_type = {
            'standard': 0,
            # save satisfies ability checks and saving throws
            'save': lambda: self.character.ability_modifiers.get(self.ability),
            # check satisfies skill checks
            'check': lambda: self.character.skill_list.skills.get(self.skill).bonus,
            # attack satisfies weapon attacks and spell attacks
            # TODO: need to work out how to determine proficiency bonus
            'attack': lambda: self.character.ability_modifiers.get(self.ability)
        }
        if self.logging:
            print(f'{self.roll_type}: {roll_type.get(self.roll_type)}')
        return roll_type.get(self.roll_type)

    def roll_dice(self):
        total_dice = []
        for dice in self.dice:
            num, sides = dice.split('d')
            total_dice.append(Dice(int(num), int(sides)))
        if self.logging:
            print(total_dice)
        result = 0
        for die in total_dice:
            result += die.roll()
        return result
    
    def get_result(self):
        return self.roll_dice() + self.roll_mod
    