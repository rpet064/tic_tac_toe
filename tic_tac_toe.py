from js import document, console
from pyscript import Element, write

turn_counter = 0
x_score = 0
y_score = 0
board_dict = {"row_one": ["", "", ""], "row_two": ["", "", ""], "row_three": ["", "", ""]}

def add_symbol(*args, **kwargs):
    global turn_counter, x_score, y_score
    symbol = "X"

    turn_counter = turn_counter + 1
    write('turn_counter', f"Turn {turn_counter}")
    write('x_score', f"X: {x_score}")
    write('y_score', f"O: {y_score}")

    if int(args[0]) < 3:
        print("first row")
    elif 3 <= int(args[0]) <= 5:
        print("second row")
    else:
        print("Third row")

    