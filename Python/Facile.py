"""
errors still to catch:
- right now whitespace doesn't throw an error (it should)
- infinite loops with GOTO
- infinite recursion with GOSUB
"""

"""
Group:
Target audience:

What unique needs did your group identify in your audience?




What choices did you make while writing your error messages to meet these needs?




Pick three error messages and add an in-line comment next to each one justifying the way you wrote it.
"""

import sys
import Helper
import Variables

def get_code():
    try:
        filename = sys.argv[1]
        code = [""]
        with open(filename) as file:
            for line in file:
                code.append(line.split())
        return code
    except IndexError:
        Helper.error()
    except FileNotFoundError:
        Helper.error()

def interpret(lines, starting_line = 1, stack = 0):
    if stack > 10:     # preventing infinitely recursive GOSUB calls
        Helper.error()
    if lines[-1] != ["."]:
        Helper.error()
    line_number = starting_line
    while line_number < len(lines):
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
                value_one = Variables.get_value(current_line[1])
                value_two = Helper.get_arg_value(current_line[2])
                Variables.set_value(current_line[1], (value_one + value_two))

            case "SUB":
                if len(current_line) != 3:
                    Helper.error()
                value_one = Variables.get_value(current_line[1])
                value_two = Helper.get_arg_value(current_line[2])
                Variables.set_value(current_line[1], (value_one - value_two))

            case "MULT":
                if len(current_line) != 3:
                    Helper.error()
                value_one = Variables.get_value(current_line[1])
                value_two = Helper.get_arg_value(current_line[2])
                Variables.set_value(current_line[1], (value_one * value_two))

            case "DIV":
                if len(current_line) != 3:
                    Helper.error()
                value_one = Variables.get_value(current_line[1])
                value_two = Helper.get_arg_value(current_line[2])
                if value_two == 0:
                    Helper.error()
                Variables.set_value(current_line[1], (value_one // value_two))

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
                if (int(current_line[5]) >= len(code) or int(current_line[5]) < 1):
                    Helper.error()
                
                conditional_one = Helper.get_arg_value(current_line[1])
                conditional_two = Helper.get_arg_value(current_line[3])
                
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
                
                if conditional:
                    line_number = int(current_line[5]) - 1
                
            case "GOSUB":
                if len(current_line) != 2:
                    Helper.error()
                if not Helper.str_is_int(current_line[1]):
                    Helper.error()
                
                new_line_number = int(current_line[1])
                if (new_line_number >= len(code) or new_line_number < 1):
                    Helper.error()
                interpret(lines, new_line_number, stack + 1)

            case "RETURN":
                if stack == 0:
                    Helper.error()
                return
            
            case "END":
                if stack != 0:
                    Helper.error()
                return
            
            case ".":
                if stack != 0:
                    Helper.error()
                exit()

            case _:
                Helper.error()
        line_number += 1


code = get_code()
interpret(code)