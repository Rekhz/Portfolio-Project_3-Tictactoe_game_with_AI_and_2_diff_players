board=[]
user_input_list=["1","2","3","4","5","6","7","8","9"]
for i in range(9):
    board.append(" ")



def print_board():
    print("_______________")
    for i in range(0,len(board),3):
        print("|",board[i],"|",board[i+1],"|",board[i+2],"|")
        print("_______________")


def check_win(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            # print(player," win")
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

def input_check(entry,board):
    if entry.isdigit():
        if 1<=int(entry)<=9:
            if board[int(entry)-1]==" ":
                return int(entry)

            else:
                entry1=input("position Already occupied,Please enter another position")
                return input_check(entry1, board)

        else:
            entry2 = input("number should not be greater than 9.enter number in range 1-9")
            return input_check(entry2, board)

    else:
        entry3 = input("enter a valid number in range 1-9")
        return input_check(entry3, board)


player_name="X"
play_game_check=True
while play_game_check:


    while " " in board:
        player_input_position=input(f"enter the position number(1-9) to enter for player {player_name}")
        check_entry=input_check(player_input_position,board)
        print(check_entry)

        board[int(check_entry)-1]=player_name
        print_board()
        check_result=check_win(player_name)
        if check_result:
            print(player_name," wins")

            break


        if " " in board:
                if player_name=="X":
                    player_name="O"
                else:
                    player_name="X"
    if " " not in board:
        print("Its a tie")
    choice = input("Do you want to continue? type yes or no:")
    if choice == "yes":
        board=[]
        for i in range(9):
            board.append(" ")
        play_game_check = True
    elif choice == "no":
        play_game_check = False
        print("Good Bye")
        exit()
    else:
        print("enter a valid response")
        print("Good Bye")
        exit()




