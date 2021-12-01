from menu import Menu
from inputActions import Input_Actions


def run():
    sample_code = [
        'CreateCharacter(Tom, D)',
        'SetExpression(Tom, Happy)',
        'SetClothing(Tom, Merchant)',
        'SetHairStyle(Tom, mage_beard)',
        'CreatePlace(SpookyPath, SpookyPath)'
        'SetPosition(Tom, SpookyPath.WestEnd)',
        'SetCameraFocus(Tom)',
    ]

    menu = Menu()
    input_action = Input_Actions(sample_code)

    menu.show_menu()

run()
