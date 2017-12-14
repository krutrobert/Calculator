from calculator import Calculator
from numpy import matrix
import datetime

def print_info():
    print('type your equation for calculation')
    print('matrix[x,y,z][a,b,c]...[u,v,m] + [x,y,z][a,b,c]...[u,v,m] - matrixes per element operations')
    print('help - set of commands')
    print('exit - close the program')
    print()

user_input = ''
calc = Calculator()
print_info()
matrix_dictionary = {}

while user_input != 'exit':
    user_input = input()
    if user_input == 'exit':
        continue
    if user_input == 'help':
        print_info()
        continue
    if len(user_input) > 0 and user_input[0] == 'v':
        continue
    if len(user_input) > 5 and user_input[0:6] == 'matrix':
        numerics_set = r'1234567890.-'
        operators_set = set(r'+-*/()')
        rows = []
        row = []
        matrix_stack = []
        current_number = ''
        counter = 0
        last_element = ''
        for symbol in user_input:
            if symbol == '[':
                row = []
                last_element = symbol
            elif symbol == ']':
                row.append(float(current_number))
                current_number = ''
                rows.append(row)
                last_element = symbol
            elif last_element != ']' and last_element != ')' and symbol in numerics_set:
                current_number += symbol
                last_element = symbol
            elif symbol == ',':
                row.append(float(current_number))
                current_number = ''
                last_element = symbol
            elif (last_element == ']' or last_element == ')') and symbol in operators_set and symbol != '(':
                if len(rows) != 0:
                    matrix_stack.append(matrix(rows))
                    rows.clear()
                matrix_stack.append(symbol)
                last_element = symbol
            elif symbol == '(':
                matrix_stack.append(symbol)
                last_element = symbol
            if counter == (len(user_input)-1) and len(rows) != 0:
                matrix_stack.append(matrix(rows))
                rows.clear()
            counter += 1
        start_time = datetime.datetime.now()
        calc.set_infix_list(matrix_stack)
        print('infix list:\n', calc.infix_list)
        print('postfix list:\n', calc.get_postfix_notation())
        print('result:\n', calc.calculate())
        stop_time = datetime.datetime.now()
        print('time elapsed:', stop_time - start_time)
        print()
        continue

    start_time = datetime.datetime.now()
    calc.set_infix_string(user_input)
    print('infix list:', calc.infix_list)
    print('postfix list:', calc.get_postfix_notation())
    print('result:', calc.calculate())
    stop_time = datetime.datetime.now()
    print('time elapsed:', stop_time - start_time)
    print()