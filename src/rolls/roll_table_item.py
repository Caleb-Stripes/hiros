class RtItem:
    def __init__(self, name: str, description: str, weight: int=1, dto: dict={}):
        self.name = name
        self.description = description
        self.weight = weight
        self.dto = dto

    def define(self):
        return {
            'name': self.name,
            'description': self.description,
            'weight': self.weight,
            'dto': self.dto
        }