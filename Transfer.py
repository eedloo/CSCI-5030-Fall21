class Transfer:
    posA = ''
    char = ''

    def transfer(self, char, posA):
        self.char = char
        self.posA = posA
        if self.posA == 'DiningRoom':
            # action('EnableInput()')
            # action(f'EnableIcon("Door", {self.posA}.Door, {self.char}, "Go to Farm!", false)')
            # action(f'EnableIcon("BackDoor", {self.posA}.BackDoor, {self.char}, "Go to Library!", false)')
            if 'Door':  # a function should be built for following codes.
                return [f'WalkTo({self.char}, {self.posA}.Door)', 'DisableInput()', f'Exit({self.char}, {self.posA}.Door, true)',
                        'FadeIn()', f'SetPosition({self.char}, Farm.Door)', 'EnableInput()']
                # action(f'WalkTo({self.char}, {self.posA}.Door)')
                # action('DisableInput()')
                # action(f'Exit({self.char}, {self.posA}.Door, true)')
                # action('FadeIn()')
                # action(f'SetPosition({self.char}, Farm.Door)')
                # action('EnableInput()')
            elif 'BackDoor':  # a function should be built for following codes.
                return [f'WalkTo({self.char}, {self.posA}.BackDoor)', 'DisableInput()', f'Exit({self.char}, {self.posA}.BackDoor, true)',
                        'FadeIn()', f'SetPosition({self.char}, Library.Door)', 'EnableInput()']
                # action(f'WalkTo({self.char}, {self.posA}.BackDoor)')
                # action('DisableInput()')
                # action(f'Exit({self.char}, {self.posA}.BackDoor, true)')
                # action('FadeIn()')
                # action(f'SetPosition({self.char}, Library.Door)')
                # action('EnableInput()')
        elif self.posA == 'Farm':
            # action('EnableInput()')
            # action(f'EnableIcon("Exit", {self.posA}.Exit, {self.char}, "Go to Library!", false)')
            if 'Exit':  # a function should be built for following codes.
                return [f'WalkTo({self.char}, {self.posA}.Exit)', 'DisableInput()', f'Exit({self.char}, {self.posA}.Exit, true)',
                        'FadeIn()', f'SetPosition({self.char}, Library.Door)', 'EnableInput()']
                # action(f'WalkTo({self.char}, {self.posA}.Exit)')
                # action('DisableInput()')
                # action(f'Exit({self.char}, {self.posA}.Exit, true)')
                # action('FadeIn()')
                # action(f'SetPosition({self.char}, Library.Door)')
                # action('EnableInput()')