from action import action
class Input_Actions:
    def __init__(self, actions):
        self.actions = actions

        for act in self.actions:
            if(act != None):
                action(act)
   
