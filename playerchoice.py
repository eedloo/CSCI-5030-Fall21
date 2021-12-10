####### PSD Project #######
##### Satish ####

from Communicator import Communicator
from inputActions import Input_Actions
from disableicon import DisableIcon

class ShowOptions(DisableIcon):
    def init(self, opt1, opt2):
        self.opt1 = opt1
        self.opt2 = opt2

    def show_options(self):
        inputs = [
            'EnableInput'
            'EnableIcon(' + self.opt1 + ', ' + self.opt1.islower() + ', DiningRoom.Door, "Go to" ' + self.opt1.islower() + '" )'
            'EnableIcon(' + self.opt1 + ', ' + self.opt1.islower() + ', DiningRoom.BackDoor, "Go to" ' + self.opt1.islower() + '" )'
            'EnableIcon(' + self.opt2 + ', ' + self.opt2.islower() + ', DiningRoom.Door, "Go to" ' + self.opt2.islower() + '" )'
            'EnableIcon(' + self.opt2 + ', ' + self.opt2.islower() + ', DiningRoom.BackDoor, "Go to" ' + self.opt2.islower() + '" )'
        ]
        input_acts = Input_Actions(inputs)

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

 
 
#testing player choice, enable_icon and disable_icon
#opt1 = "Forest"
#opt2 = "Bookshelf"
#show_opt = ShowOptions(opt1, opt2)
#show_opt.show_options()
#selected_option = show_opt.get_selected_option()
#show_opt.disable_icon(selected_option)
