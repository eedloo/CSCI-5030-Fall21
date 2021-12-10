class Perform:
    char1 = ''
    char2 = ''
    item = ''
    furniture = ''

    def dance(self, char1, char2):
        self.char1 = char1
        self.char2 = char2
        return [f'DanceTogether({self.char1}, {self.char2})']

    def give(self, char1, item, char2):
        self.char1 = char1
        self.item = item
        self.char2 = char2
        return [f'Give({self.char1}, {self.item}, {self.char2})']

    def attack(self, char1, char2):
        self.char1 = char1
        self.char2 = char2
        return [f'Attack({self.char1}, {self.char2}, true)']

    def pickup(self, char1, item, furniture):
        self.char1 = char1
        self.item = item
        self.furniture = furniture
        return [f'Pickup({self.char1}, {self.item}, {self.furniture})']

    # def open_furniture(self, char1, furniture):
    #    self.char1 = char1
    #    self.furniture = furniture
    #    return [f'OpenFurniture({self.char1}, {self.furniture})']

    def set_camera(self, char1):
        self.char1 = char1
        return [f'SetCameraFocus({self.char1})']

    def set_position(self, char1, furniture):
        # furniture can be objects like table, or it can be places like farm, or character`s hand.
        # char1 can be both items or characters.
        self.char1 = char1
        self.furniture = furniture
        return [f'SetPosition({self.char1}, {self.furniture})']

    def enable_input(self):
        # enable input to move with WASD and mouse buttons
        return [f'EnableInput']












