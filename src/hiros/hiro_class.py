import math

class HiroClass:
    def __init__(self, name: str, ability_scores: 'AbilityScores', character_level=1):
        self.name = name
        self.character_level = character_level
        self.proficiency_bonus = self.calc_prof_bonus(character_level)
        self.ability_scores = ability_scores
        self.ability_modifiers = ability_scores.modifiers()
        self.skill_list = SkillList(self.ability_modifiers, self.proficiency_bonus)
        
    def __str__(self):
        return self.name
    
    def level_up(self):
        self.character_level += 1
        before_prof = self.proficiency_bonus
        self.proficiency_bonus = self.calc_prof_bonus(self.proficiency_bonus)
        if before_prof != self.proficiency_bonus:
            for skill in self.skills:
                skill.update_proficiency_bonus(self.proficiency_bonus)
                
    def calc_prof_bonus(self, level):
        calc = math.ceil(self.character_level / 4) + 1
        if calc > 2:
            return calc
        return 2
    
    def update_skill_proficiency(self, skill_name, proficiency: str):
        self.skill_list.skills[skill_name].update_prof(proficiency)
        
    def update_ability_score(self, ability: str, value: int):
        self.ability_scores.update(ability, value)
        self.ability_modifiers = self.ability_scores.modifiers()
        
    def get_mod(self, ability=None):
        if ability:
            return {self.ability_modifiers.get(ability)}
        return self.ability_modifiers
        
        
class AbilityScores:
    def __init__(self, strength: int, dexterity: int, constitution: int, intelligence: int, wisdom: int, charisma: int) -> None:
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = dexterity
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        
    def update(self, ability, value):
        setattr(self, ability, value)
        
    def modifiers(self):
        def calc_mod(base_score):
            return math.floor((base_score - 10) / 2)
        return {
            'STR': calc_mod(self.strength),
            'DEX': calc_mod(self.dexterity),
            'CON': calc_mod(self.constitution),
            'INT': calc_mod(self.intelligence),
            'WIS': calc_mod(self.wisdom),
            'CHA': calc_mod(self.charisma)
        }
        
class Skill:
    def __init__(self, name: str, ability_mod: int, proficiency: str= 'none', proficiency_bonus: int=2) -> None:
        self.name = name
        self.ability_mod = ability_mod
        self.proficiency = proficiency
        self.proficiency_bonus = proficiency_bonus
        self.bonus = self.calc_bonus()
        
    def calc_bonus(self):
        proficiencies = {
            'none': lambda: self.ability_mod,
            'proficient': lambda: self.ability_mod + self.proficiency_bonus,
            'expert': lambda: self.ability_mod + (self.proficiency_bonus * 2)
        }
        prof = proficiencies.get(self.proficiency)
        return prof()
    
    def update_prof(self, new_proficiency='none'):
        self.proficiency = new_proficiency
        self.bonus = self.calc_bonus()
        
    def update_prof_bonus(self, proficiency_bonus):
        self.proficiency_bonus = proficiency_bonus
        self.bonus = self.calc_bonus()
        
        
class SkillList:
    def __init__(self, ability_modifiers: dict, proficiency_bonus: int) -> None:
        self.skills = {
            'Acrobatics': Skill('Acrobatics', ability_modifiers['DEX'], 'none', proficiency_bonus),
            'Animal Handling': Skill('Animal Handling', ability_modifiers['WIS'], 'none', proficiency_bonus),
            'Arcana': Skill('Arcana', ability_modifiers['INT'], 'none', proficiency_bonus),
            'Athletics': Skill('Athletics', ability_modifiers['STR'], 'none', proficiency_bonus),
            'Deception': Skill('Deception', ability_modifiers['CHA'], 'none', proficiency_bonus),
            'History': Skill('History', ability_modifiers['INT'], 'none', proficiency_bonus),
            'Insight': Skill('Insight', ability_modifiers['WIS'], 'none', proficiency_bonus),
            'Intimidation': Skill('Intimidation', ability_modifiers['CHA'], 'none', proficiency_bonus),
            'Investigation': Skill('Investigation', ability_modifiers['INT'], 'none', proficiency_bonus),
            'Medicine': Skill('Medicine', ability_modifiers['WIS'], 'none', proficiency_bonus),
            'Nature': Skill('Nature', ability_modifiers['INT'], 'none', proficiency_bonus),
            'Perception': Skill('Perception', ability_modifiers['WIS'], 'none', proficiency_bonus),
            'Performance': Skill('Performance', ability_modifiers['CHA'], 'none', proficiency_bonus),
            'Persuasion': Skill('Persuasion', ability_modifiers['CHA'], 'none', proficiency_bonus),
            'Religion': Skill('Religion', ability_modifiers['INT'], 'none', proficiency_bonus),
            'Sleight of Hand': Skill('Sleight of Hand', ability_modifiers['DEX'], 'none', proficiency_bonus),
            'Stealth': Skill('Stealth', ability_modifiers['DEX'], 'none', proficiency_bonus),
            'Survival': Skill('Survival', ability_modifiers['WIS'], 'none', proficiency_bonus),
        }
    