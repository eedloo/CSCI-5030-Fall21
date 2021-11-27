from action import action

def wait_for(msg):
    while True:
        receivedmsg = input()
        if receivedmsg == msg:
            return True
        elif receivedmsg == 'input Selected Credits':
            action('SetCredits(Reza!)')
            action('ShowCredits()')
        elif receivedmsg == 'input Selected Quit':
            action('Quit()')
        elif receivedmsg == 'input Close Credits':
            action('HideCredits()')


def show_menu():
    action ('ShowMenu()')
    wait_for('input Selected Start')
    action('HideMenu()')