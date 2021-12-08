class Transfer:
    char = ''
    posA = ''
    posA_exit = ''
    posB = ''
    posB_enter = ''

    def goto (self, char, posA, posA_exit, posB, posB_enter):
        self.char = char
        self.posA = posA
        self.posA_exit = posA_exit
        self.posB = posB
        self.posB_enter = posB_enter

        return [f'WalkTo({self.char}, {self.posA}.{self.posA_exit})', 'DisableInput()',
                f'Exit({self.char}, {self.posA}.{self.posA_exit}, true)',
                f'Enter({self.char}, {self.posB}.{self.posB_enter}, true)', 'EnableInput()']

