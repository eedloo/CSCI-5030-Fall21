from action import action


def pickup(char='', obj='', objspawnpos=''):
    # action('EnableInput()')
    action(f'WalkTo({char}, {objspawnpos})')
    action(f'EnableIcon({obj}, {obj}, {obj}, "Pick it up!", false)')
    action(f'Pickup({char}, {obj}, {objspawnpos})')

