####### PSD Project #######
##### Satish ####
from inputActions import Input_Actions


class DisableIcon:
    def disable_icon(self, option):
        input_acts = Input_Actions()
        if option == self.opt1:
            inputs = ['DisableIcon(' + self.opt1 + ', DiningRoom.Door)']
            inputs = ['DisableIcon(' + self.opt1 + ', DiningRoom.BackDoor)']
            input_acts.get_actions(inputs)

        else:
            inputs = ['DisableIcon(' + self.opt2 + ', DiningRoom.Door)']
            inputs = ['DisableIcon(' + self.opt2 + ', DiningRoom.BackDoor)']
            input_acts.get_actions(inputs)
