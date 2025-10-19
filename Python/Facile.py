"""
errors still to catch:
- no input in terminal
- file not found
- lowercase letters
- right now whitespace doesn't throw an error (it should)
- goto'ing to a line past end of code
"""

import sys
import Helper
import Variables

operators = ["=", "<>", "<", ">", "<=", ">="]

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
                Variables.set_value(current_line[1], current_line[2])
                break
            case "PRINT":
                if len(current_line) != 2:
                    Helper.error()
                try:
                    print(f"{Variables.get_value(current_line[1])}")
                except KeyError:
                    Helper.error()
                break
            case "ADD":
                if len(current_line) != 3:
                    Helper.error()
                try:
                    value_one = Variables.get_value(current_line[1])
                    if Helper.str_is_int(current_line[2]):
                        value_two = int(current_line[2])
                    else:
                        value_two = Variables.get_value(current_line[2])
                    Variables.set_value(current_line[1], (value_one + value_two))
                except KeyError:
                    Helper.error()
                break
            case "SUB":
                if len(current_line) != 3:
                    Helper.error()
                try:
                    value_one = Variables.get_value(current_line[1])
                    if Helper.str_is_int(current_line[2]):
                        value_two = int(current_line[2])
                    else:
                        value_two = Variables.get_value(current_line[2])
                    Variables.set_value(current_line[1], (value_one - value_two))
                except KeyError:
                    Helper.error()
                break
            case "MULT":
                if len(current_line) != 3:
                    Helper.error()
                try:
                    value_one = Variables.get_value(current_line[1])
                    if Helper.str_is_int(current_line[2]):
                        value_two = int(current_line[2])
                    else:
                        value_two = Variables.get_value(current_line[2])
                    Variables.set_value(current_line[1], (value_one * value_two))
                except KeyError:
                    Helper.error()
                break
            case "DIV":
                if len(current_line) != 3:
                    Helper.error()
                try:
                    value_one = Variables.get_value(current_line[1])
                    if Helper.str_is_int(current_line[2]):
                        value_two = int(current_line[2])
                    else:
                        value_two = Variables.get_value(current_line[2])
                    if value_two == 0:
                        Helper.error()
                    Variables.set_value(current_line[1], (value_one // value_two))
                except KeyError:
                    Helper.error()
                break
            case "GOTO":
                if len(current_line) != 2:
                    Helper.error()
                try:
                    new_line_number = int(current_line[1]) - 1
                    if new_line_number >= len(code):
                        Helper.error()
                    line_number = new_line_number
                except ValueError:
                    Helper.error()
                break
            case "IF":
                if len(current_line) != 6:
                    Helper.error()