"""
errors still to catch:
- no input in terminal
- file not found
- lowercase letters
- right now whitespace doesn't throw an error (it should)
"""

import sys
import Helper
from Variables import Variable
from string import ascii_uppercase as alphabet

operators = ["=", "<>", "<", ">", "<=", ">="]
variable_dict = {}
for letter in alphabet:
    variable_dict.update({letter: Variable(letter)})


filename = sys.argv[1]
code = [""]
with open(filename) as file:
    for line in file:
        code.append(line.split())

def interpret(lines, starting_line = 1):
    line_number = starting_line
    while line_number <= len(lines):
        current_line = lines[line_number]
        match current_line[0]:
            case "LET":
                if len(current_line) != 3:
                    Helper.error()
                variable_dict[current_line[1]] = current_line[2]
                break
            case "PRINT":
                if len(current_line) != 2:
                    Helper.error()
                try:
                    print(f"{variable_dict[current_line[1]]}")
                except KeyError:
                    Helper.error()
            case "ADD":
                if len(current_line) != 3:
                    Helper.error()
                try:
                    value_one = variable_dict[current_line[1]].get_value()
                    if Helper.str_is_int(current_line[2]):
                        value_two = int(current_line[2])
                        variable_dict[current_line[1]].set_value(value_one + value_two)
                    else:
                        value_two = variable_dict[current_line[2]].get_value()
                        variable_dict[current_line[1]].set_value(value_one + value_two)
                except KeyError:
                    Helper.error()   
            case "SUB":
                if len(current_line) != 3:
                    Helper.error()
                try:
                    value_one = variable_dict[current_line[1]].get_value()
                    if Helper.str_is_int(current_line[2]):
                        value_two = int(current_line[2])
                        variable_dict[current_line[1]].set_value(value_one - value_two)
                    else:
                        value_two = variable_dict[current_line[2]].get_value()
                        variable_dict[current_line[1]].set_value(value_one - value_two)
                except KeyError:
                    Helper.error()
            case "MULT":
                if len(current_line) != 3:
                    Helper.error()
                try:
                    value_one = variable_dict[current_line[1]].get_value()
                    if Helper.str_is_int(current_line[2]):
                        value_two = int(current_line[2])
                        variable_dict[current_line[1]].set_value(value_one * value_two)
                    else:
                        value_two = variable_dict[current_line[2]].get_value()
                        variable_dict[current_line[1]].set_value(value_one * value_two)
                except KeyError:
                    Helper.error()
            case "DIV":
                if len(current_line) != 3:
                    Helper.error()
                try:
                    value_one = variable_dict[current_line[1]].get_value()
                    if Helper.str_is_int(current_line[2]):
                        value_two = int(current_line[2])
                    else:
                        value_two = variable_dict[current_line[2]].get_value()
                    if value_two == 0:
                        Helper.error()
                    variable_dict[current_line[1]].set_value(value_one // value_two)
                except KeyError:
                    Helper.error()