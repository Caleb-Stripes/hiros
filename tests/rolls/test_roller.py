import unittest
from unittest.mock import patch
from rolls.roller import Roller
from hiros.hiro_class import HiroClass, AbilityScores

class TestRoller(unittest.TestCase):
    def setUp(self):
        self.hiro = HiroClass('Hiro', AbilityScores(12,11,12,13,14,16))
    
    def tearDown(self):
        return super().tearDown
    
    def test_Roller_init(self):
        test_roller = Roller(character=self.hiro, roll_type='standard', ability='STR', logging=True, dice=['1d20'])
        self.assertEqual(test_roller.dice, ['1d20'])
        
    def test_Roller_calc_mod_standard(self):
        test_roller = Roller(character=self.hiro, roll_type='standard', ability='STR')
        mod = test_roller.calc_mod()
        self.assertEqual(mod(), 0)
        
    def test_Roller_calc_mod_save(self):
        test_roller = Roller(character=self.hiro, roll_type='save', ability='STR')
        mod = test_roller.calc_mod()
        self.assertEqual(mod(), self.hiro.ability_modifiers.get('STR'))
        
    def test_Roller_calc_mod_check(self):
        test_roller = Roller(character=self.hiro, roll_type='check', skill='Athletics')
        mod = test_roller.calc_mod()
        self.assertEqual(mod(), self.hiro.skill_list.skills.get('Athletics').bonus)
        
    def test_Roller_calc_mod_attack(self):
        test_roller = Roller(character=self.hiro, roll_type='attack', ability='STR', skill='Athletics')
        mod = test_roller.calc_mod()
        self.assertEqual(mod(), self.hiro.ability_modifiers.get('STR'))
        
    @patch('rolls.dice.Dice.roll')
    def test_Roller_roll_dice(self, mock_dice_roll):
        mock_dice_roll.return_value = 10
        test_roller = Roller(character=self.hiro, roll_type='standard', ability='STR', logging=True, dice=['1d20', '1d20'])
        actual = test_roller.roll_dice()
        self.assertEqual(actual, 20)
    
    @patch('rolls.dice.Dice.roll')    
    def test_Roller_get_result(self, mock_dice_roll):
        mock_dice_roll.return_value = 6
        test_roller = Roller(character=self.hiro, roll_type='standard', ability='STR', logging=True, dice=['1d20', '1d20'])
        self.assertEqual(test_roller.get_result(), 12)