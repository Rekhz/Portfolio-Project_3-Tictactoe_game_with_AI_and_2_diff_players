board = []
user_input_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
for i in range(9):
    board.append(" ")


def print_board():
    print("_______________")
    for i in range(0, len(board), 3):
        print("|", board[i], "|", board[i + 1], "|", board[i + 2], "|")
        print("_______________")


def check_win(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True


def input_check(entry, board):
    if entry.isdigit():
        if 1 <= int(entry) <= 9:
            if board[int(entry) - 1] == " ":
                return int(entry)
            else:
                entry1 = input("Position already occupied. Please enter another position: ")
                return input_check(entry1, board)
        else:
            entry2 = input("Number should not be greater than 9. Enter a number in the range 1-9: ")
            return input_check(entry2, board)
    else:
        entry3 = input("Enter a valid number in the range 1-9: ")
        return input_check(entry3, board)


def minimax(board,is_maximizer):
    if check_win("O"):
        return 10
    elif check_win("X"):
        return - 10
    elif " " not in board:
        return 0

    if is_maximizer:

        max_eval = -100
        for i in range(len(board)):
            if board[i] == " ":
                board[i] = "O"
                eval_score = minimax(board,False)
                board[i] = " "
                max_eval = max(max_eval, eval_score)
        return max_eval
    else:
        min_eval = 100
        for i in range(len(board)):
            if board[i] == " ":
                board[i] = "X"
                eval_score = minimax(board,True)
                board[i] = " "
                min_eval = min(min_eval, eval_score)
        return min_eval
player_name = "X"
play_game_check = True
while play_game_check:
    win_is_there_or_not=False
    while " " in board:
        if player_name == "X":
            player_input_position = input(f"Enter the position number (1-9) to enter for player {player_name}: ")
            current_entry = input_check(player_input_position, board)
        else:
            best_score = -100
            best_pos = 0
            for i in range(len(board)):
                if board[i] == " ":
                    board[i] = "O"
                    eval_score = minimax(board,False)
                    board[i] = " "
                    if eval_score > best_score:
                        best_score = eval_score
                        best_pos = i
            current_entry = best_pos + 1

        board[int(current_entry) - 1] = player_name
        print_board()
        check_result = check_win(player_name)
        if check_result:
            print(player_name, "wins")
            win_is_there_or_not=True
            break
        if " " in board:
            if player_name == "X":
                player_name = "O"
            else:
                player_name = "X"
    if " " not in board and not win_is_there_or_not:
        print("It's a tie")

    choice = input("Do you want to continue? Type 'yes' or 'no': ")
    if choice == "yes":
        board = []
        for i in range(9):
            board.append(" ")
        play_game_check = True
    elif choice == "no":
        play_game_check = False
        print("Goodbye!")
        exit()
    else:
        print("Enter a valid response")
        print("Goodbye!")
        exit()
