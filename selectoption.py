from playerchoice import ShowOption
class GetSelectedOption(Showoptions):
   def get_selected_option(slef):
       comm = Communication()
       selected_option = comm.get_input_from_player()
       return selected_option
