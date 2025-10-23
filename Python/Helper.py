def error():
    print("ERROR.")
    exit()

def str_is_int(string):
    try:
        new = int(string)
        return True
    except ValueError:
        return False