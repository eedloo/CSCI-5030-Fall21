from action import Action
class Input_Actions(Action):
    def __init__(self, actions):
        self.actions = actions

        for act in self.actions:
            if(act != None):
                self.action(act)
