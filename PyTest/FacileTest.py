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
import HelperTest
import VariablesTest

def get_code():
    try:
        filename = sys.argv[1]
        code = [""]
        with open(filename) as file:
            for line in file:
                code.append(line.split())
        return code
    except IndexError:
        HelperTest.error("no file")
    except FileNotFoundError:
        HelperTest.error("file not found", filename)

def interpret(lines, starting_line = 1, stack = 0):
    if stack > 20:     # preventing infinitely recursive GOSUB calls
        HelperTest.error("infinite recursion", None, starting_line)
    if lines[-1] != ["."]:
        HelperTest.error("no period", None, len(lines) - 1)
    line_number = starting_line
    while line_number < len(lines):
        current_line = lines[line_number]
        match current_line[0]:
            case "LET":
                if len(current_line) != 3:
                    HelperTest.error("param error", len(current_line), line_number, "let")
                VariablesTest.set_value(current_line[1], current_line[2], line_number)

            case "PRINT":
                if len(current_line) != 2:
                    HelperTest.error("param error", len(current_line), line_number, "print")
                print(f"{VariablesTest.get_value(current_line[1], line_number)}")

            case "ADD":
                if len(current_line) != 3:
                    HelperTest.error("param error", len(current_line), line_number, "add")
                value_one = VariablesTest.get_value(current_line[1], line_number)
                value_two = HelperTest.get_arg_value(current_line[2], line_number)
                VariablesTest.set_value(current_line[1], (value_one + value_two), line_number)

            case "SUB":
                if len(current_line) != 3:
                    HelperTest.error("param error", len(current_line), line_number, "sub")
                value_one = VariablesTest.get_value(current_line[1], line_number)
                value_two = HelperTest.get_arg_value(current_line[2], line_number)
                VariablesTest.set_value(current_line[1], (value_one - value_two), line_number)

            case "MULT":
                if len(current_line) != 3:
                    HelperTest.error("param error", len(current_line), line_number, "mult")
                value_one = VariablesTest.get_value(current_line[1], line_number)
                value_two = HelperTest.get_arg_value(current_line[2], line_number)
                VariablesTest.set_value(current_line[1], (value_one * value_two), line_number)

            case "DIV":
                if len(current_line) != 3:
                    HelperTest.error("param error", len(current_line), line_number, "div")
                value_one = VariablesTest.get_value(current_line[1], line_number)
                value_two = HelperTest.get_arg_value(current_line[2], line_number)
                if value_two == 0:
                    HelperTest.error("div by zero", current_line[2], line_number, current_line[1])
                VariablesTest.set_value(current_line[1], (value_one // value_two), line_number)

            case "GOTO":
                if len(current_line) != 2:
                    HelperTest.error("param error", len(current_line), line_number, "goto")
                if not HelperTest.str_is_int(current_line[1]):
                    HelperTest.error("line not int", current_line[1], line_number, "GOTO")
                new_line_number = int(current_line[1]) - 1
                if (new_line_number >= len(code) or new_line_number < 1):
                    HelperTest.error("invalid jump", new_line_number, line_number, len(code) - 1)
                line_number = new_line_number

            case "IF":
                if len(current_line) != 6:
                    HelperTest.error("param error", len(current_line), line_number, "if")
                if current_line[4] != "THEN":
                    HelperTest.error("no then", current_line[4], line_number)
                if not HelperTest.str_is_int(current_line[5]):
                    HelperTest.error("line not int", current_line[5], line_number, "IF")
                if (int(current_line[5]) >= len(code) or int(current_line[5]) < 1):
                    HelperTest.error("invalid jump", current_line[5], line_number, len(code) - 1)
                
                conditional_one = HelperTest.get_arg_value(current_line[1], line_number)
                conditional_two = HelperTest.get_arg_value(current_line[3], line_number)
                
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
                        HelperTest.error("invalid operator", current_line[2], line_number)
                
                if conditional:
                    line_number = int(current_line[5]) - 1
                
            case "GOSUB":
                if len(current_line) != 2:
                    HelperTest.error("param error", len(current_line), line_number, "gosub")
                if not HelperTest.str_is_int(current_line[1]):
                    HelperTest.error("line not int", current_line[1], line_number, "GOSUB")
                
                new_line_number = int(current_line[1])
                if (new_line_number >= len(code) or new_line_number < 1):
                    HelperTest.error("invalid jump", new_line_number, line_number, len(code) - 1)
                interpret(lines, new_line_number, stack + 1)

            case "RETURN":
                if len(current_line) != 1:
                    HelperTest.error("param error", len(current_line), line_number, "return")
                if stack == 0:
                    HelperTest.error("invalid return", None, line_number)
                return
            
            case "END":
                if len(current_line) != 1:
                    HelperTest.error("param error", len(current_line), line_number, "end")
                if stack != 0:
                    HelperTest.error("end in stack", "END", line_number)
                return
            
            case ".":
                if len(current_line) != 1:
                    HelperTest.error("param error", len(current_line), line_number, ".")
                if stack != 0:
                    HelperTest.error("end in stack", ".", line_number)
                exit()

            case _:
                HelperTest.error("invalid input", current_line[0], line_number)
        line_number += 1


code = get_code()
interpret(code)