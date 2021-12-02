class Char:
    name = ''
    clothing = ''
    hairStyle = ''
    hairColor = ''
    typ = ''
    init_position = ''

    def create_char(self, name, typ, clothing, hairStyle, hairColor, init_position):
        self.Name = name
        self.Type = typ
        self.Clothing = clothing
        self.HairStyle = hairStyle
        self.HairColor = hairColor
        self.init_position = init_position
        return [f'CreateCharacter({self.Name}, {self.Type})', f'SetClothing({self.Name}, {self.Clothing})',
                f'SetHairStyle({self.Name}, {self.HairStyle})', f'SetHairColor({self.Name}, {self.HairColor})', f'SetPosition({self.Name}, {self.init_position})']
