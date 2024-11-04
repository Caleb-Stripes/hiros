from dice import Dice


class RollTable:
    def __init__(self, table_name: str='new_table', table_data: list=[{0,0}]):
        self.table_name = table_name
        self.table_data = table_data
        
    def roll(self):
        return self.table_data[Dice(1, len(self.table_data)).roll()]
        
        
    def add_item(self, name: str, description: str, weight: int=1, dto: dict={}):
        i = weight
        while i > 0:
            self.table_data.append(RtItem(name, description, weight, dto))
            i -= 1
 
        
class RtItem:
    def __init__(self, name: str, description: str, weight: int=1, dto: dict={}):
        self.name = name
        self.description = description
        self.weight = weight
