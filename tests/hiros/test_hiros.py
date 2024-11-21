import unittest

from hiros.hiro_class import HiroClass, AbilityScores, SkillList

class TestHiroClass(unittest.TestCase):
    def setUp(self):
        self.hiro = HiroClass('Hiro', AbilityScores(10,10,10,10,10,10))
    def tearDown(self):
        return super().tearDown()
    
    def test_HiroClass_init(self):
        self.assertEqual(self.hiro.name, 'Hiro')
        self.assertEqual(self.hiro.character_level, 1)
        self.assertEqual(self.hiro.proficiency_bonus, 2)
        
        self.assertEqual(self.hiro.ability_scores.strength, 10)
        self.assertEqual(self.hiro.ability_scores.dexterity, 10)
        self.assertEqual(self.hiro.ability_scores.constitution, 10)
        self.assertEqual(self.hiro.ability_scores.intelligence, 10)
        self.assertEqual(self.hiro.ability_scores.wisdom, 10)
        self.assertEqual(self.hiro.ability_scores.charisma, 10)
        
        self.assertEqual(self.hiro.ability_modifiers.get('STR'), 0)
        self.assertEqual(self.hiro.ability_modifiers.get('DEX'), 0)
        self.assertEqual(self.hiro.ability_modifiers.get('CON'), 0)
        self.assertEqual(self.hiro.ability_modifiers.get('INT'), 0)
        self.assertEqual(self.hiro.ability_modifiers.get('WIS'), 0)
        self.assertEqual(self.hiro.ability_modifiers.get('CHA'), 0)
        
        self.assertIsInstance(self.hiro.skill_list, SkillList)
        
    def test_HiroClass_str_(self):
        self.assertEqual(str(self.hiro), 'Hiro')
        
    def test_HiroClass_level_up(self):
        self.hiro.level_up()
        self.assertEqual(self.hiro.character_level, 2)
        self.assertEqual(self.hiro.proficiency_bonus, 2)
        
    def test_HiroClass_update_skill_proficiency(self):
        self.hiro.update_skill_proficiency('Athletics', 'proficient')
        self.assertEqual(self.hiro.skill_list.skills['Athletics'].proficiency, 'proficient')