class Transfer:
    posA = ''
    char = ''

    def transfer(self, char, posA):
        self.char = char
        self.posA = posA
        if self.posA == 'DiningRoom':
            if 'Door':  
                return [f'WalkTo({self.char}, {self.posA}.Door)', 'DisableInput()', f'Exit({self.char}, {self.posA}.Door, true)',
                        'FadeIn()', f'SetPosition({self.char}, Farm.Door)', 'EnableInput()']
                
            elif 'BackDoor':  
                return [f'WalkTo({self.char}, {self.posA}.BackDoor)', 'DisableInput()', f'Exit({self.char}, {self.posA}.BackDoor, true)',
                        'FadeIn()', f'SetPosition({self.char}, Library.Door)', 'EnableInput()']
                
        elif self.posA == 'Farm':
            if 'Exit':  
                return [f'WalkTo({self.char}, {self.posA}.Exit)', 'DisableInput()', f'Exit({self.char}, {self.posA}.Exit, true)',
                        'FadeIn()', f'SetPosition({self.char}, Library.Door)', 'EnableInput()']
                
