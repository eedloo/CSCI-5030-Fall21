
#Interating with Camelot by unsing input commands
def action(input_command):
    print('start ' + input_command)
    return check_success(input_command)

#Check with the Camelot whther the command succeeded or failed
def check_success(input_command):
    while True:
        received = input()
        if received == 'succeeded ' + input_command:
            return True
        elif received.startswith('failed ' + input_command):
            return False
        elif received.startswith('error ' + input_command):
            return False