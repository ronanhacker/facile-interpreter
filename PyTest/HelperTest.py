import VariablesTest

def error(error_code=None, input=None, line_number=None, second_code=None):
    if line_number:
        print(f"Error: Line {line_number}")
    else:
        print("Error:")
    match error_code:
        case "no period":
            print(f"The final line of the program must be a period.")
        case "infinite recursion":
            print(f"The program has terminated after entering more than twenty recursive GOSUB statements.\nRemember to terminate GOSUB with RETURN.")
        case "invalid operator":
            print(f"{input} is not a valid operator in an IF statement.\nValid operators: =, <>, <, >, <=, >=")
        case "invalid input":
            print(f"{input} is not a recognized command.\nMake sure the command is spelled correctly and all letters are capitalized.")
        case "end in stack":
            print(f"Program was terminated with {input} while still within a GOSUB statement.\nExit the GOSUB with RETURN before terminating the program.")
        case "invalid return":
            print(f"A return was encountered outside of a GOSUB statement.\nTry terminating the program with END before entering the GOSUB.")
        case "no then":
            print(f"Fourth parameter of IF must be THEN.\nIt is currently {input}.")
        case "div by zero":
            print(f"Cannot divide {second_code} by {input}.\n{input} is equal to zero.")
        case "invalid jump":
            print(f"Cannot jump to line {input}.\nProgram is of length {second_code}.")
        case "line not int":
            print(f"Line numbers in {second_code} must be integers.\n{input} is not a valid line number.")
        case "no file":
            print("Input a Facile file to interpret.")
        case "file not found":
            print(f"The file {input} was not found.\nMake sure your file is in the correct directory.")
        case "param error":
            match second_code:
                case "add":
                    func_name = "ADD"
                    params = 2
                case "sub":
                    func_name = "SUB"
                    params = 2
                case "div":
                    func_name = "DIV"
                    params = 2
                case "mult":
                    func_name = "MULT"
                    params = 2
                case "let":
                    func_name = "LET"
                    params = 2
                case "print":
                    func_name = "PRINT"
                    params = 1
                case "goto":
                    func_name = "GOTO"
                    params = 1
                case "if":
                    func_name = "IF"
                    params = 5
                case "gosub":
                    func_name = "GOSUB"
                    params = 1
                case "return":
                    func_name = "RETURN"
                    params = 0
                case "end":
                    func_name = "END"
                    params = 0
                case ".":
                    func_name = "."
                    params = 0
                case _:
                    func_name = "uh oh scoob!!"
                    params = 100
            if (params > 1 or params == 0) and (input > 2 or input == 1):
                print(f"The {func_name} function takes {params} parameters.\nIt is currently receiving {input - 1} parameters.")
            elif (params > 1 or params == 0) and (input == 2):
                print(f"The {func_name} function takes {params} parameters.\nIt is currently receiving {input - 1} parameter.")
            elif (params == 1) and (input > 2 or input == 1):
                print(f"The {func_name} function takes {params} parameter.\nIt is currently receiving {input - 1} parameters.")
            else:
                print(f"The {func_name} function takes {params} parameter.\nIt is currently receiving {input - 1} parameter.")
        case "var not int":
            print(f"Cannot set variable to value {input}.\nAll variables must be set to integer values.")
        case "uninit var":
            print(f"The variable {input} has not been initiaized.\nAll variables must be initialized with a LET statement before being referenced.")
        case "unreal var":
            print(f"The variable {input} does not exist.\nRecall that all variables are uppercase letters A-Z.")
        case _:
            print("ERROR.")
    exit()

def str_is_int(string):
    try:
        new = int(string)
        return True
    except ValueError:
        return False

def get_arg_value(string, line_number):
    if str_is_int(string):
        return int(string)
    return VariablesTest.get_value(string, line_number)