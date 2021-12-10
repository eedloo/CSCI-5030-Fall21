from action import Action
class Input_Actions:

    def get_actions(self, actions):
            action_object = Action()
            for act in actions:
                if (act != None):
                    action_object.action(act)
