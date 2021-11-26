def check_for_success(command):
    while True:
        received = input()
        if received == 'succeeded ' + command:
            return True
        elif received.startswith('failed ' + command):
            return False

def action(command):
    print('start ' + command)
    return check_for_success(command)
