from Place import Place
from Char import Char
from inputActions import Input_Actions
from ActionFunctions import Perform
from playerchoice import ShowOptions
from menu import Menu
from disableicon import DisableIcon

#Show Menu
menu = Menu()
menu.show_menu()

input_act = Input_Actions()
perform = Perform()

#create DiningRoom
place = Place()
dining_room=place.create_place('DiningRoom', 'DiningRoom')
input_act.get_actions(dining_room)

#create character Tom
tom=Char()
char_tom = (tom.create_char('Tom', 'D', 'Merchant', 'Short', 'Black', 'DiningRoom'))
input_act.get_actions(char_tom)

#SetCamera
input_act.get_actions(perform.set_camera('Tom'))

#Enable Icon
choice = ShowOptions("Bookshelf", "Forest")
choice.show_options()

#Disable Icon

disable = DisableIcon()

#Enable Input
input_act.get_actions(perform.enable_input())


while (True):
    input()


