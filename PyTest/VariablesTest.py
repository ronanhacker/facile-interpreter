import HelperTest
from string import ascii_uppercase as alphabet

variable_dict = {letter: None for letter in alphabet}

def get_value(variable, line_number):
    if variable not in variable_dict:
        HelperTest.error("unreal var", variable, line_number)
    if variable_dict[variable] == None:
        HelperTest.error("uninit var", variable, line_number)
    return variable_dict[variable]

def set_value(variable, value, line_number):
    if variable not in alphabet:
        HelperTest.error("unreal var", variable, line_number)
    try:
        variable_dict[variable] = int(value)
    except ValueError:
        HelperTest.error("var not int", value, line_number)