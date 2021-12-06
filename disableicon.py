####### PSD Project #######
##### Satish ####

class DisableIcon:
   def disable_icon(self, option):
       if option == self.opt1:
           inputs = [ 'DisableIcon(' + self.opt1 + ', Tom )' ]
           input_acts = Input_Actions(inputs)
           menu.show_menu()
        else:
           inputs = [ 'DisableIcon(' + self.opt2 + ', Tom )' ]
           input_acts = Input_Actions(inputs)
           menu.show_menu()
