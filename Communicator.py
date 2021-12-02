from action import action


class Communicator:
    def get_input_from_player(self):
        while True:
            receivedmsg = input()
            if receivedmsg == 'input Bookshelf Tom':
                action('DisableIcon("Forest", Tom)')
                action('DisableIcon("Bookshelf", Tom)')
                return "Library"
            elif receivedmsg == 'input Forest Tom':
                action('DisableIcon("Forest", Tom)')
                action('DisableIcon("Bookshelf", Tom)')
                return "Farm"
            elif receivedmsg == 'input Book Tom':
                action('DisableIcon("Sword", Tom)')
                action('DisableIcon("Book", Tom)')
                return "Book"
            elif receivedmsg == 'input Sword Tom':
                action('DisableIcon("Sword", Tom)')
                action('DisableIcon("Book", Tom)')
                return "Sword"