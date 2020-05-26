# check if the player has won after a move
def checkwin(board):
    for row in range(3):
        vcheck = 0
        hcheck = 0
        rcheck = 0
        ccheck = 0
        for col in range(3):
            if board[row][col] == "X":
                hcheck += 1
            if board[col][row] == "X":
                vcheck += 1
            if board[row][col] == "O":
                rcheck += 1
            if board[col][row] == "O":
                ccheck += 1
        if vcheck == 3 or hcheck == 3:
            return "X"
        elif ccheck == 3 or rcheck == 3:
            return "O"

    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        return "X"
    if board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X":
        return "X"
    if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        return "O"
    if board[2][0] == "O" and board[1][1] == "O" and board[0][2] == "O":
        return "O"
    return "N"


# printing the game board
def printboard(board):
    print(board[0][0] + " " + board[0][1] + " " + board[0][2])
    print(board[1][0] + " " + board[1][1] + " " + board[1][2])
    print(board[2][0] + " " + board[2][1] + " " + board[2][2])


# game code
def playgame():
    player = "O"
    count = 0
    while checkwin(game) == "N":
        if count == 9:
            player = 'no one'
            break
        if player == "O":
            player = "X"
        else:
            player = "O"
        print("\nHere's the board")
        printboard(game)
        while True:
            move = input("Player " + player + ", please make your move: ")
            r = 2 - int((int(move) - 1) / 3)
            c = round((int(move) % 3 + 2) % 3)
            if game[r][c] == '•':
                game[r][c] = player
                break
            else:
                print("You can't go there")
        count += 1

    if player != "no one":
        player = "player " + player
    print("\n\nGame over, " + player + " has won.")
    printboard(game)


# setup/instructions
game = [['7', '8', '9'],
        ['4', '5', '6'],
        ['1', '2', '3']]
print("Here's how the board works...")
printboard(game)

# start game
while True:
    game = [['•', '•', '•'],
            ['•', '•', '•'],
            ['•', '•', '•']]
    playgame()
    userChoice = input("Enter y to play again, anything else to quit game: ")
    if userChoice != 'y':
        break
