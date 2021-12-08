class Char:
    def __init__(self, name, clothing, hairStyle, hairColor,  typ, init_position )
    name = self.name
    clothing = self.clothing
    hairStyle = self.hairStyle
    hairColor = self.hairColor
    typ = self.typ
    init_position = self.init_position

    def create_char(self):
        return [f'CreateCharacter({self.name}, {self.typ})', f'SetClothing({self.name}, {self.clothing})',
                f'SetHairStyle({self.name}, {self.hairStyle})', f'SetHairColor({self.name}, {self.hairColor})', f'SetPosition({self.name}, {self.init_position})']
