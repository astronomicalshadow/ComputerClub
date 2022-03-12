# I just use tridecimal counting or something because I was to lazy to figure out what 10, 11, and 12's number should be
backupBoard = [[" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
               [" | ", "   ", "(A)", "   ", "(B)", "   ", "(C)", "   ", "(D)", " | "],
               [" | ", "(E)", "   ", "(F)", "   ", "(G)", "   ", "(H)", "   ", " | "],
               [" | ", "   ", "(I)", "   ", "(J)", "   ", "(K)", "   ", "(L)", " | "],
               [" | ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " | "],
               [" | ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " | "],
               [" | ", "[A]", "   ", "[B]", "   ", "[C]", "   ", "[D]", "   ", " | "],
               [" | ", "   ", "[E]", "   ", "[F]", "   ", "[G]", "   ", "[H]", " | "],
               [" | ", "[I]", "   ", "[J]", "   ", "[K]", "   ", "[L]", "   ", " | "],
               [" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "]]

board = [[" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
         [" | ", "   ", "(A)", "   ", "(B)", "   ", "(C)", "   ", "(D)", " | "],  # # # # # # # # # #
         [" | ", "(E)", "   ", "(F)", "   ", "(G)", "   ", "(H)", "   ", " | "],  # Player 1  Pieces
         [" | ", "   ", "(I)", "   ", "(J)", "   ", "(K)", "   ", "(L)", " | "],  #
         [" | ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " | "],
         [" | ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " | "],
         [" | ", "[A]", "   ", "[B]", "   ", "[C]", "   ", "[D]", "   ", " | "],  # # # # # # # # # #
         [" | ", "   ", "[E]", "   ", "[F]", "   ", "[G]", "   ", "[H]", " | "],  # Player 2 Pieces
         [" | ", "[I]", "   ", "[J]", "   ", "[K]", "   ", "[L]", "   ", " | "],  #
         [" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "]]
boardSize = [10, 10]

# First 12 positions are player 1's pieces and last 12 positions are player 2's pieces
# In sub arrays, positions are stored as [y, x]
backupPiecesPos = [[1, 2], [1, 4], [1, 6], [1, 8],
                   [2, 1], [2, 3], [2, 5], [2, 7],
                   [3, 2], [3, 4], [3, 6], [3, 8],

                   [6, 1], [6, 3], [6, 5], [6, 7],
                   [7, 2], [7, 4], [7, 6], [7, 8],
                   [8, 1], [8, 5], [8, 5], [8, 7]]

piecesPos = [[1, 2], [1, 4], [1, 6], [1, 8],  # # # # # # # # # #
             [2, 1], [2, 3], [2, 5], [2, 7],  # Player 1 Pieces
             [3, 2], [3, 4], [3, 6], [3, 8],  #

             [6, 1], [6, 3], [6, 5], [6, 7],  # # # # # # # # # #
             [7, 2], [7, 4], [7, 6], [7, 8],  # Player 2 Pieces
             [8, 1], [8, 5], [8, 5], [8, 7]]  #


# r - row | c - column
def draw():
    r = 0
    c = 0

    global board
    global boardSize
    global piecesPos

    while r <= boardSize[0] - 1:
        while c <= boardSize[1] - 1:
            print(board[r][c], end="")
            c += 1
        c = 0
        r += 1
        print(end="\n")

playerTurn = "1"
def askMove():
    if playerTurn == "1":
        playerInput = input("Player 1, what piece would you like to move and where (Format: \"<piece char> <dir (UL, UR, DL, DR)>\") - \n")
    else:
        playerInput = input("Player 2, what piece would you like to move and where (Format: \"<piece char> <dir (UL, UR, DL, DR)>\") - \n")

    move = [playerInput[0], (playerInput[2] + playerInput[3])]
    return move

backupPiecesDict = {
    "(A)": 0,
    "(B)": 1,
    "(C)": 2,
    "(D)": 3,
    "(E)": 4,
    "(F)": 5,
    "(G)": 6,
    "(H)": 7,
    "(I)": 8,
    "(J)": 9,
    "(K)": 10,
    "(L)": 11,
    "[A]": 12,
    "[B]": 13,
    "[C]": 14,
    "[D]": 15,
    "[E]": 16,
    "[F]": 17,
    "[G]": 18,
    "[H]": 19,
    "[I]": 20,
    "[J]": 21,
    "[K]": 22,
    "[L]": 23,
}

piecesDict = {
    "(A)": 0,
    "(B)": 1,
    "(C)": 2,
    "(D)": 3,
    "(E)": 4,
    "(F)": 5,
    "(G)": 6,
    "(H)": 7,
    "(I)": 8,
    "(J)": 9,
    "(K)": 10,
    "(L)": 11,
    "[A]": 12,
    "[B]": 13,
    "[C]": 14,
    "[D]": 15,
    "[E]": 16,
    "[F]": 17,
    "[G]": 18,
    "[H]": 19,
    "[I]": 20,
    "[J]": 21,
    "[K]": 22,
    "[L]": 23,
}


# Checks if the piece can move in the desired direction
def move():
    global piecesPos
    global boardSize
    global piecesDict
    global playerTurn

    playerInput = askMove()

    # Properly formats piece to work with dic(t)
    if playerTurn == "1":
        playerInput[0] = "(" + playerInput[0] + ")"
    else:
        playerInput[0] = "[" + playerInput[0] + "]"

    dirDict = {
        "UL": [-1, -1],
        "UR": [-1, 1],
        "DL": [1, -1],
        "DR": [1, 1]
    }

    # Assigns input to easy to read vars
    piece, dir = playerInput[0], playerInput[1]
    dir = dirDict[dir]

    currentPos = [piecesPos[piecesDict[piece]][0], piecesPos[piecesDict[piece]][1]]
    nextPos = [piecesPos[piecesDict[piece]][0] + dir[0], piecesPos[piecesDict[piece]][1] + dir[1]]


    # 0 - Can't move | 1 - Move | 2 - Jump
    if nextPos > boardSize or nextPos < [0, 0]:
        print("You can't move there. Please try again.")

    elif board[nextPos[0]][nextPos[1]] == "   ":
        if playerTurn == "1":
            playerTurn = "2"
        else:
            playerTurn = "1"
        board[currentPos[0]][currentPos[1]] = "   "
        board[nextPos[0]][nextPos[1]] = piece
        piecesPos[piecesDict[piece]] = nextPos

    elif nextPos[0] + dir[0] > boardSize[0] or nextPos[0] < 0 or nextPos[1] + dir[1] > boardSize[1] or nextPos[1] < 0:
        print("You can't move there. Please try again.")

    elif board[nextPos[0] + dir[0]][nextPos[1] + dir[1]] == "   " and piece[0] != board[nextPos[0]][nextPos[1]][0]:
        if playerTurn == "1":
            score[0] += 1
            playerTurn = "2"
        else:
            score[1] += 1
            playerTurn = "1"

        board[currentPos[0]][currentPos[1]] = "   "
        board[nextPos[0] + dir[0]][nextPos[1] + dir[1]] = piece
        piecesPos[piecesDict[piece]][0], piecesPos[piecesDict[piece]][1] = nextPos[0] + dir[0], nextPos[1] + dir[1]

        piecesDict.pop(board[nextPos[0]][nextPos[1]])
        board[nextPos[0]][nextPos[1]] = "   "

    else:
        print("You can't move there. Please try again.")


win = False
score = [11, 0]
while not win:
    draw()
    move()
    if score[0] == 12:
        draw()
        print("Player one wins!")
        win = False if input("Would you like to play again (y/n) - ") != "n" else True

        board = backupBoard
        piecesPos = backupPiecesPos
        piecesDict = backupPiecesDict

    elif score[1] == 12:
        draw()
        print("Player two wins!")
        win = False if input("Would you like to play again (y/n) - ") != "n" else True

        board = backupBoard
        piecesPos = backupPiecesPos
        piecesDict = backupPiecesDict
