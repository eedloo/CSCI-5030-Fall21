####### PSD Project #######
##### Satish ####

from Communicator import Communicator
from inputActions import Input_Actions
from disableicon import DisableIcon


class ShowOptions(DisableIcon):
    def __init__(self, opt1, opt2):
        self.opt1 = opt1
        self.opt2 = opt2

    def show_options(self):
        inputs = [
            'EnableInput',
            'EnableIcon(' + self.opt1 + ', ' + str(self.opt1.lower()) + ', DiningRoom.Door, "Go to " ' + self.opt1 + ' )',
            'EnableIcon(' + self.opt1 + ', ' + str(self.opt1.lower()) + ', DiningRoom.BackDoor, "Go to" ' + self.opt1 + '" )',
            'EnableIcon(' + self.opt2 + ', ' + str(self.opt2.lower())+ ', DiningRoom.Door, "Go to" ' + self.opt2+ '" )',
            'EnableIcon(' + self.opt2 + ', ' + str(self.opt2.lower()) + ', DiningRoom.BackDoor, "Go to" ' + self.opt2 + '" )'
        ]

        input_acts = Input_Actions()
        input_acts.get_actions(inputs)

    def get_selected_option(self):
        comm = Communicator()
        selected_option = comm.get_input_from_player()
        return selected_option

    def walking_to_door(self):
        option = Communicator()
        selected = option.get_input_from_player()
        if selected == "Library":
            return 'WalkTo(Tom, DiningRoom.Door)'
        else:
            return 'WalkTo(Tom, DiningRoom.BackDoor)'
