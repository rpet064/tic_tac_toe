from pyscript import write, Element

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
        clicked_btn = Element(f'btn{user_input}')
        write(clicked_btn, "X")
        return "X"
    
    else: 

        # add styled text to "user_input (clicked_button)"
        clicked_btn = Element(f'btn{user_input}')
        write(clicked_btn, "O")
        return "O"
