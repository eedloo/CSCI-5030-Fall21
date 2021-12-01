from action import action


class Menu:
    def wait_for(self, msg):
        while True:
            receivedmsg = input()
            if receivedmsg == msg:
                return True
            elif receivedmsg == 'input Selected Credits':
                action('SetCredits(This is a project for Principle of Software Development Class that is done by '
                       'Reza, Mohsen, Satish and Anjani.)')
                action('ShowCredits()')
            elif receivedmsg == 'input Selected Quit':
                action('Quit()')
            elif receivedmsg == 'input Close Credits':
                action('HideCredits()')

    def show_menu(self):
        action('ShowMenu()')
        self.wait_for('input Selected Start')
        action('HideMenu()')
