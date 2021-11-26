#########Game Setup#########
#Author: Mohsen
#Instantiate Characters, Places, Objects

from action import action

def Instantiation():
    action('SetTitle(\"Princess Killers: PSD Class Project\")', False)
    action("SetCredits(\"Experience Manager by Mohsen, Reza, Satish, Anjani\")", False)

    ##########Create characters##########

    #Tom
    action('CreateCharacter(Tom, B)')
    action('SetHairStyle(Tom, Long)', False)
    action('SetEyeColor(Tom, blue)', False)
    action('SetPosition(Tom, DiningRoom)', False)


    #Kate
    action('CreateCharacter(Kate, A)')
    action('SetClothing(Kate, Noble)', False)
    action('SetHairStyle(Kate, Straight)', False)
    action('SetHairColor(Kate, Brown)', False)
    action('SetPosition(Kate, Farm.Well)', False)

    ##########Create Places##########

    action('CreatePlace(TomsRoom, Cottage)')
    action('CreatePlace(Farm, Farm)')
    action('CreatePlace(Lib, Library)')

    ##########Create Objects##########

    action('CreateItem(Hammer, Hammer)')
    action('SetPosition(Hammer, Table.Surface)', False)

    action('CreateItem(Book, GreenBook)')
    action('SetPosition(Hammer, Library.AlchemistTable.Surface.Left)', False)

    # Setup beginning of the game
def game_setup():
    Instantiation()

    # Show the menu
    action('ShowMenu()')






