import unittest
from unittest.mock import patch
from rolls.dice import Die,Dice

class TestDie(unittest.TestCase):
    def tearDown(self):
        return super().tearDown
    
    def test_Die_init(self):
        die = Die(2)
        self.assertEqual(die.sides, 2)
    
    @patch('random.randint')
    def test_Die_roll(self, mock_randint):
        mock_randint.return_value = 2
        die = Die(2)
        self.assertEqual(die.roll(), 2)
        

class TestDice(unittest.TestCase):
    def tearDown(self):
        return super().tearDown
    
    def test_Dice_init(self):
        dice = Dice(2, 2)
        self.assertEqual(dice.number, 2)
        self.assertEqual(dice.sides, 2)
        
    @patch('rolls.dice.Die.roll')
    def test_Dice_roll(self, mock_die_roll):
        mock_die_roll.return_value = 2
        dice = Dice(2, 2)
        self.assertEqual(dice.roll(), 4)