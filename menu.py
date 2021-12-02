from action import Action


class Menu(Action):
    def wait_for(self, msg):
        while True:
            receivedmsg = input()
            if receivedmsg == msg:
                return True
            elif receivedmsg == 'input Selected Credits':
                self.action('SetCredits(This is a project for Principle of Software Development Class that is done by '
                       'Reza, Mohsen, Satish and Anjani.)')
                self.action('ShowCredits()')
            elif receivedmsg == 'input Selected Quit':
                self.action('Quit()')
            elif receivedmsg == 'input Close Credits':
                self.action('HideCredits()')

    def show_menu(self):
        self.action('ShowMenu()')
        self.wait_for('input Selected Start')
        self.action('HideMenu()')
