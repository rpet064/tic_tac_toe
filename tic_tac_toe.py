from pyscript import Element, write
import utils

# global gamestate variables
turn_counter = 0
reset_scores = False

# seperated into rows of 3 to show how is rendered in index.html
board_array = [
    "", "", "",
    "", "", "",
    "", "", ""
]

# This array contains all the possible winning solutions
# solutions 0, 1 & 2 are horizontal, 3, 4, 5 - vertical, 6 & 7 are diagonal
winning_combinations = {
    "solution0": [0, 1, 2],
    "solution1": [3, 4, 5],
    "solution2": [6, 7, 8],
    "solution3": [0, 3, 6],
    "solution4": [1, 4, 7],
    "solution5": [2, 5, 8],
    "solution6": [0, 4, 8],
    "solution7": [2, 4, 6]
}

def add_symbol(*args, **kwargs):
    global turn_counter, board_array, winning_combinations, reset_scores

    # even turns (0, 2, 4, 6) is X players's turn
    x_turn = turn_counter % 2 == 0

    # takes first (and only) input from args tuple passed from buttons
    user_input = args[0]

    # check if array position where user clicked is empty
    if board_array[user_input] == "":

        # Update turn counter if user clicks on empty space on board
        turn_counter = turn_counter + 1
        board_array[user_input] = utils.add_symbol(x_turn, user_input)
        
        # Check if winners on turn 5 (first possible turn with winning combination)
        if  (5 <= turn_counter <= 8):

            # Loop through all possible (7) winning combinations
            for key, value in winning_combinations.items():

                # checks if there are symbols in these positons
                if board_array[value[0]] != "" and board_array[value[1]] != "" and board_array[value[2]] != "":

                    # checks these symbols are all the same
                    if board_array[value[0]] == board_array[value[1]] == board_array[value[2]]:

                        # break the loop, add points to the winning X team and update score div
                        if board_array[value[0]] == "X":
                            utils.update_x_score()

                        # add points to the winning Y team and update score div
                        else: 
                            utils.update_o_score()
                        
                        # Reset Turn Counter & Gameboard
                        board_array = utils.reset_board(reset_scores)
                        turn_counter = 0
        elif turn_counter == 9:
    
            # Reset Turn Counter & Gameboard - as the board is full
            board_array = utils.reset_board(reset_scores)
            turn_counter = 0

