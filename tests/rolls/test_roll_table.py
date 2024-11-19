import unittest
from unittest.mock import patch
from rolls.roll_table import RollTable
from rolls.roll_table_item import RtItem

class TestRollTable(unittest.TestCase):
    def setUp(self):
        self.roll_table = RollTable()
        
    def tearDown(self):
        return super().tearDown()
    
    def test_roll_table_init(self):
        self.assertIsInstance(self.roll_table, RollTable)
        self.assertEqual(self.roll_table.table_name, 'new_table')
        
    def test_add_item(self):
        self.roll_table.add_item('Potion of Healing', 'Heals 5 hp', weight=5)
        self.assertEqual(self.roll_table.table_data[1].name, 'Potion of Healing')
        self.assertEqual(self.roll_table.table_data[1].description, 'Heals 5 hp')
        self.assertEqual(self.roll_table.table_data[1].weight, 5)
        self.assertEqual(self.roll_table.table_data[1].dto, {})
        
    def test_add_rt_item(self):
        rt_item = RtItem('Potion of Healing', 'Heals 5 hp', weight=5)
        self.roll_table.add_rt_item(rt_item)
        self.assertEqual(self.roll_table.table_data[1].name, 'Potion of Healing')
        self.assertEqual(self.roll_table.table_data[1].description, 'Heals 5 hp')
        self.assertEqual(self.roll_table.table_data[1].weight, 5)
        self.assertEqual(self.roll_table.table_data[1].dto, {})
        
    def test_rt_item_define(self):
        rt_item = RtItem('Potion of Healing', 'Heals 5 hp', weight=5)
        self.assertEqual(rt_item.define(), {
            'name': 'Potion of Healing',
            'description': 'Heals 5 hp',
            'weight': 5,
            'dto': {}})
        
    @patch('rolls.dice.Dice.roll')
    def test_roll_table_roll(self, mock_dice_roll):
        mock_dice_roll.return_value = 2
        self.roll_table.add_item('Potion of Healing', 'Heals 5 hp', weight=5)
        expected = self.roll_table.table_data[2]
        result = self.roll_table.roll()
        self.assertEqual(result, expected)
        
        