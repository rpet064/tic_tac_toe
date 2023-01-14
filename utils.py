from pyscript import Element
from js import document

x_score = 0
o_score = 0

def reset_board(reset_scores):

    global x_score, o_score

    # Reset button ids
    for i in range (0, 9):
        btn = Element(f'btn{i}')
        btn.remove_class("x-bg-colour")
        btn.remove_class("o-bg-colour")


    # Clear text from buttons
    for i in range (0, 9):
        btn = Element(f'btn{i}')
        btn.element.innerHTML = ("")

    # reset board array
    board_array = [
                    "", "", "",
                    "", "", "",
                    "", "", ""
                 ]

    # check if needs to reset scores
    if reset_scores:
        x_score = 0
        o_score = 0
        x_scoreboard = Element('x_score')
        x_scoreboard.element.innerHTML = f"X: {x_score} points"
        o_scoreboard = Element('o_score')
        o_scoreboard.element.innerHTML = f"O: {o_score} points"


    return board_array


def add_symbol(x_turn, user_input):
    if (x_turn):

        # add styled text to "user_input (clicked_button)"
        btn = Element(f'btn{user_input}')
        btn.element.innerHTML = ("X")
        btn.add_class("x-bg-colour")
        return "X"
    
    else: 

        # add styled text to "user_input (clicked_button)"
        btn = Element(f'btn{user_input}')
        btn.element.innerHTML = ("O")
        btn.add_class("o-bg-colour")
        return "O"

def update_x_score():
    global x_score
    x_score += 1
    x_scoreboard = Element('x_score')

    # check if "points are plural or singular"
    if x_score == 1:
        x_scoreboard.element.innerHTML = f"X: {x_score} point"
    else:
        x_scoreboard.element.innerHTML = f"X: {x_score} points"
        
    return x_score

def update_o_score():
    global o_score
    o_score += 1
    o_scoreboard = Element('o_score')

    # check if "points are plural or singular"
    if o_score == 1:
        o_scoreboard.element.innerHTML = f"O: {o_score} point"
    else:
        o_scoreboard.element.innerHTML = f"O: {o_score} points"

    return o_score

