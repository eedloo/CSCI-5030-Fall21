class Char:
    name = ''
    clothing = ''
    hairStyle = ''
    hairColor = ''
    typ = ''
    init_position = ''

    def create_char(self, name, typ, clothing, hairStyle, hairColor, init_position):
        self.name = name
        self.typ = typ
        self.clothing = clothing
        self.hairStyle = hairStyle
        self.hairColor = hairColor
        self.init_position = init_position
        return [f'CreateCharacter({self.name}, {self.typ})', f'SetClothing({self.name}, {self.clothing})',
                f'SetHairStyle({self.name}, {self.hairStyle})', f'SetHairColor({self.name}, {self.hairColor})',
                f'SetPosition({self.name}, {self.init_position})']
