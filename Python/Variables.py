import Helper
from string import ascii_uppercase as alphabet

variable_dict = {letter: None for letter in alphabet}

def get_value(variable):
    if variable not in variable_dict:
        Helper.error()
    if variable_dict[variable] == None:
        Helper.error()
    return variable_dict[variable]

def set_value(variable, value):
    if variable not in alphabet:
        Helper.error()
    try:
        int_value = int(value)
        variable_dict[variable] = int_value
    except ValueError:
        Helper.error()