from pyscript import Element, write

# global gamestate variables
turn_counter = 0
x_score = 0
o_score = 0

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
    global turn_counter, x_score, o_score, board_array, winning_combinations

    # even turns (0, 2, 4, 6) is X players's turn
    x_turn = turn_counter % 2 == 0

    # takes first (and only) input from args tuple passed from buttons
    user_input = args[0]

    # check if array position where user clicked is empty
    if board_array[user_input] == "":

        # Update turn counter if user clicks on empty space on board
        turn_counter = turn_counter + 1

        if (x_turn):
            board_array[user_input] = "X"
            write(f'btn{user_input}', "X")
        else: 
            board_array[user_input] = "O"
            write(f'btn{user_input}', "O")
        
        # Check if winners on turn 5 (first possible turn with winning combination)
        if turn_counter >= 5:

            # Loop through all possible (7) winning combinations
            for key, value in winning_combinations.items():

                # checks if there are symbols in these positons
                if board_array[value[0]] != "" and board_array[value[1]] != "" and board_array[value[2]] != "":

                    # checks these symbols are all the same
                    if board_array[value[0]] == board_array[value[1]] == board_array[value[2]]:

                        # break the loop, add points to the winning X team and update score div
                        if board_array[value[0]] == "X":
                            x_score += 1

                            # check if "points are plural or singular"
                            if x_score == 1:
                                write('x_score', f"X: {x_score} point")
                            else:
                                write('x_score', f"X: {x_score} points")

                        # add points to the winning Y team and update score div
                        else: 
                            o_score += 1
                            write('y_score', f"O: {o_score} Point")

                            # check if "points are plural or singular"
                            if o_score == 1:
                                write('y_score', f"O: {o_score} point")
                            else:
                                write('y_score', f"O: {o_score} points")
                        
                        # Reset Turn Counter & Gameboard
                        turn_counter = 0
                        board_array = [
                                        "", "", "",
                                        "", "", "",
                                        "", "", ""
                                    ]
                        for i in range (0, 9):
                            write(f'btn{i}', "")

