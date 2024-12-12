def input_string(message):
    x = str(input(message))
    return x

def input_integer(message):
    x = int(input(message))
    return x

def input_real(message):
    x = float(input(message))
    return x

def input_boolean(message):
    x = input(message)
    if not x in ['y', 'n']:
        return 'No option like this!'
    else:
        return True if x == 'y' else False