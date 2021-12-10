from inputActions import Input_Actions


class Communicator:

    def get_input_from_player(self):
        input_action=Input_Actions()
        while True:
            receivedmsg = input()
            if receivedmsg == 'input Bookshelf Tom':
                return "Bookshelf"
            elif receivedmsg == 'input Forest Tom':
                return "Forest"
            elif receivedmsg == 'input Book Tom':
                return "Book"
            elif receivedmsg == 'input Sword Tom':
                return "Sword"
