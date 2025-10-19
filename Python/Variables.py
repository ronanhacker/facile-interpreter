import Helper
from string import ascii_uppercase as alphabet

variable_dict = {}
for letter in alphabet:
    variable_dict.update({letter: None})

def get_value(variable):
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