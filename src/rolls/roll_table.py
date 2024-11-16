from rolls.dice import Dice
from rolls.roll_table_item import RtItem


class RollTable:
    def __init__(self, table_name: str='new_table', table_data: list=[{0,0}]):
        self.table_name = table_name
        self.table_data = table_data
        
    def roll(self):
        numb = Dice(1, len(self.table_data)-1).roll()
        print(numb)
        return self.table_data[numb]
        
        
    def add_item(self, name: str, description: str, weight: int=1, dto: dict={}):
        i = weight
        while i > 0:
            self.table_data.append(RtItem(name, description, weight, dto))
            i -= 1
    
    
    def add_rt_item(self, rt_item: RtItem):
        self.add_item(rt_item.name, rt_item.description, rt_item.weight, rt_item.dto)
        