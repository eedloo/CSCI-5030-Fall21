from Communicator import Communicator
from inputActions import Input_Actions
from selectedoption import getSelectedOption
class ShowOptions(getSelectedOptions):
   def init(self, opt1, opt2):
       self.opt1 = opt1
       self.opt2 = opt2
   def show_options(self):
       inputs = [
               'EnableInput'
               'EnableIcon(' + self.opt1 + ', ' + self.opt1.islower() +', Tom, "Go to" '+ self.opt1.islower() + '" )'
               'EnableIcon(' + self.opt2 + ', ' + self.opt2.islower() +', Tom, "Go to" '+ self.opt2.islower() + '" )'
               ]
       input_acts = Input_Actions(inputs)
       menu.show_menu()


#testing player choice, enable_icon and disable_icon 
opt1 = "Forest"
opt2 = "Bookshelf"
show_opt = ShowOptions(opt1, opt2)
show_opt.show_options()
selected_option = show_opt.get_selected_option()
show_opt.disable_icon(selected_option)
