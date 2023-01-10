from pyscript import write

def reset_board():

    # Clear text from buttons
    for i in range (0, 9):
        write(f'btn{i}', "")

    # reset board array
    board_array = [
                    "", "", "",
                    "", "", "",
                    "", "", ""
                 ]
    return board_array


def add_symbol(x_turn, user_input):
    if (x_turn):

        # add styled text to "user_input (clicked_button)"
        write(f'btn{user_input}', "X")
        return "X"
    
    else: 

        # add styled text to "user_input (clicked_button)"
        write(f'btn{user_input}', "O")
        return "O"

def update_x_score(x_score):
    x_score =+ 1

    # check if "points are plural or singular"
    if x_score == 1:
        write('x_score', f"X: {x_score} point")
    else:
        write('x_score', f"X: {x_score} points")
        
    return x_score

def update_o_score(o_score):
    o_score =+ 1
    write('y_score', f"O: {o_score} Point")

    # check if "points are plural or singular"
    if o_score == 1:
        write('y_score', f"O: {o_score} point")
    else:
        write('y_score', f"O: {o_score} points")

    return o_score

