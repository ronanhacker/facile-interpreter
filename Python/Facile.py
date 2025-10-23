"""
errors still to catch:
- lowercase letters
- right now whitespace doesn't throw an error (it should)
- goto'ing to a line past end of code
- referencing a variable not a-z
- no return in gosub, extra return out of gosub
- no period at end
"""

import sys
import Helper
import Variables

def interpret(lines, starting_line = 1):
    line_number = starting_line
    while line_number <= len(lines):
        current_line = lines[line_number]
        match current_line[0]:
            case "LET":
                if len(current_line) != 3:
                    Helper.error()
                Variables.set_value(current_line[1], current_line[2])

            case "PRINT":
                if len(current_line) != 2:
                    Helper.error()
                print(f"{Variables.get_value(current_line[1])}")

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

            case "GOTO":
                if len(current_line) != 2:
                    Helper.error()
                if not Helper.str_is_int(current_line[1]):
                    Helper.error()
                new_line_number = int(current_line[1]) - 1
                if (new_line_number >= len(code) or new_line_number < 1):
                    Helper.error()
                line_number = new_line_number

            case "IF":
                if len(current_line) != 6:
                    Helper.error()
                if current_line[4] != "THEN":
                    Helper.error()
                if not Helper.str_is_int(current_line[5]):
                    Helper.error()
                if (current_line[5] >= len(code) or current_line[5] < 1):
                    Helper.error()
                
                if Helper.str_is_int(current_line[1]):
                    conditional_one = str(current_line[1])
                else:
                    conditional_one = Variables.get_value[current_line[1]]
                
                if Helper.str_is_int(current_line[3]):
                    conditional_two = str(current_line[3])
                else:
                    conditional_two = Variables.get_value[current_line[3]]
                
                match current_line[2]:
                    case "=":
                        conditional = conditional_one == conditional_two
                    case "<>":
                        conditional = conditional_one != conditional_two
                    case "<":
                        conditional = conditional_one < conditional_two
                    case ">":
                        conditional = conditional_one > conditional_two
                    case "<=":
                        conditional = conditional_one <= conditional_two
                    case ">=":
                        conditional = conditional_one >= conditional_two
                    case _:
                        Helper.error()
                
                if conditional == True:
                    line_number = int(current_line[5]) - 1
                
            case "GOSUB":
                if len(current_line) != 2:
                    Helper.error()
                if not Helper.str_is_int(current_line[1]):
                    Helper.error()
                
                new_line_number = int(current_line[1])
                if (new_line_number >= len(code) or new_line_number < 1):
                    Helper.error()

                interpret(lines, new_line_number)

            case "RETURN":
                return
            
            case "END":
                return
            
            case ".":
                SystemExit

            case _:
                Helper.error()
        line_number += 1


try:
    filename = sys.argv[1]
    code = [""]
    with open(filename) as file:
        for line in file:
            code.append(line.split())
except IndexError:
    Helper.error()
except FileNotFoundError:
    Helper.error()

interpret(code)