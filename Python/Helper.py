def error():
    print("ERROR.")
    SystemExit

def str_is_int(string):
    try:
        return int(string)
    except ValueError:
        return False