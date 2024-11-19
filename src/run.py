from hiros.hiro_class import HiroClass, AbilityScores
from rolls.roll_table import RollTable, RtItem
from rolls.roller import Roller

def main():
    
    ######## HIRO ########
    # scores = AbilityScores(15,10,13,8,12,14)
    # einar = HiroClass('Einar', scores)
    # smite = Roller(character=einar, roll_type='standard', ability='CHA', logging=True, dice=['3d8', '1d10'])
    # climb = Roller(character=einar, roll_type='attack', ability='STR', skill='Athletics')
    # import pdb; pdb.set_trace()
    
    ######## ROLL TABLE ########
    rt = RollTable('loot')
    potion = RtItem('Potion of Healing', 'Heals 5 hp', weight=5)
    coin = RtItem('Coin', '1 cp', weight=10)
    sword = RtItem('Sword', '1d6 damage', weight=5)
    magical_sword = RtItem('Magical Sword', '1d8 damage', weight=1)
    rt.add_rt_item(potion)
    rt.add_rt_item(coin)    
    rt.add_rt_item(sword)
    rt.add_rt_item(magical_sword)
    print(rt.table_data)
    for item in rt.table_data[1:]:
        print(item.define())

    i=10
    while i > 0:
        print(rt.roll().define())
        i -= 1
if __name__ == "__main__":
    main()
    