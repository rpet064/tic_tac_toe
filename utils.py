from pyscript import Element
from js import document

# Global Variables
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
        btn.add_class("x-bg-colour")
        btn.element.innerHTML = "X"
        return "X"
    
    else: 

        # add styled text to "user_input (clicked_button)"
        btn = Element(f'btn{user_input}')
        btn.add_class("o-bg-colour")
        btn.element.innerHTML = ("O")
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

def check_end_of_game():
    global x_score, o_score

    # Reset scores as end of game
    if x_score == 2:
        reset_board(reset_scores = True)
        return True

    elif o_score == 2:
        reset_board(reset_scores = True)
        return True

    reset_board(reset_scores = False)
    return False


def hide_modal(modal_id):
    modal = Element(modal_id)
    modal.add_class("hide_modal")
    modal.remove_class("show_modal")


def show_modal(modal_id):
    modal = Element(modal_id)
    modal.add_class("show_modal")
    modal.remove_class("hide_modal")


def end_of_round_animation(end_of_round_outcome):
        show_modal("end-round-modal")


def end_of_game_animation(end_of_game_outcome):
        show_modal("end-game-modal")



