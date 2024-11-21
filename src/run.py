from hiros.hiro_class import HiroClass, AbilityScores
from rolls.roll_table import RollTable, RtItem
from rolls.roller import Roller

def main():
    einar = HiroClass('Einar', AbilityScores(15,16,12,8,10,14))
    roll_table = RollTable()
    roll_table.add_item('Potion of Healing', 'Heals 5 hp', weight=5)
    roll_table.add_rt_item(RtItem('Common Sword', 'Deals 1d6 slashing damage', weight=10))
    roll_table.add_rt_item(RtItem('Common Dagger', 'Deals 1d4 piercing damage', weight=10))
    roll_table.add_rt_item(RtItem('Arcane Hand Cannon', 'Deals 1d10 fire damage', weight=1))
    
    
    print('dir(einar):', dir(einar))
    print('')
    print('dir(roll_table):', dir(roll_table))
    print('')
    import pdb; pdb.set_trace()

if __name__ == "__main__":
    main()
    