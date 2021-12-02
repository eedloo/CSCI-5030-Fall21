# Interacting with Camelot by using input commands

class Action:

    def action(self, input_command):
        print('start ' + input_command)
        #return check_success(input_command)

    # Check with the Camelot whether the command succeeded or failed
    def check_success(self, input_command):
        while True:
            received = input()
            if received == 'succeeded ' + input_command:
                return True
            elif received.startswith('failed ' + input_command):
                return False
            elif received.startswith('error ' + input_command):
                return False
