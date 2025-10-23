import Variables

def error():
    print("ERROR.")
    exit()

def str_is_int(string):
    try:
        new = int(string)
        return True
    except ValueError:
        return False

def get_arg_value(string):
    if str_is_int(string):
        return int(string)
    return Variables.get_value(string)