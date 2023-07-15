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
winning_combinations = {
    # Horizontal winning solutions
    "solution0": [0, 1, 2],
    "solution1": [3, 4, 5],
    "solution2": [6, 7, 8],

    # Vertical winning solutions
    "solution3": [0, 3, 6],
    "solution4": [1, 4, 7],
    "solution5": [2, 5, 8],

    # Diagonal winning solutions
    "solution6": [0, 4, 8],
    "solution7": [2, 4, 6]
}

def execute_turn(*args, **kwargs):
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
        if  (5 <= turn_counter <= 9):

            # Loop through all possible (7) winning combinations
            for key, value in winning_combinations.items():

                # checks if there are symbols in these positons
                if board_array[value[0]] != "" and board_array[value[1]] != "" and board_array[value[2]] != "":

                    # checks these symbols are all the same
                    if board_array[value[0]] == board_array[value[1]] == board_array[value[2]]:

                        # break loop, add points to winning X team, update score div and check if end of game
                        if board_array[value[0]] == "X":
                            utils.update_x_score()
                            end_of_game = utils.check_end_of_game()

                            if (end_of_game):
                                utils.end_of_game_animation("x")
                            else:
                                utils.end_of_round_animation("x")

                        # break loop, add points to winning O team, update score div and check if end of game
                        else: 
                            utils.update_o_score()
                            end_of_game = utils.check_end_of_game()

                            if (end_of_game):
                                utils.end_of_game_animation("o")
                            else:
                                utils.end_of_round_animation("o")                        
                        
                        # Reset Turn Counter & Gameboard
                        board_array = utils.reset_board(reset_scores = False)
                        turn_counter = 0
                    
                    # Reset board as there is no winner
                    elif turn_counter == 9:
                        board_array = utils.reset_board(reset_scores = False)
                        turn_counter = 0
                        utils.end_of_round_animation("draw")                        


def reset_game():
    utils.reset_board(reset_scores = True)


def hide_modal(modal_id):
    utils.hide_modal(modal_id)
    


