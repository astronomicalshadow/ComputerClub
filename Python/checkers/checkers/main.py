# I just use tridecimal counting or something because I was to lazy to figure out what 10, 11, and 12's number should be
board = [[" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
         [" | ", "   ", "(1)", "   ", "(2)", "   ", "(2)", "   ", "(4)", " | "], # # # # # # # # # #
         [" | ", "(5)", "   ", "(6)", "   ", "(7)", "   ", "(8)", "   ", " | "], # Player 1  Pieces
         [" | ", "   ", "(9)", "   ", "(A)", "   ", "(B)", "   ", "(C)", " | "], #
         [" | ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " | "],
         [" | ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " | "],
         [" | ", "   ", "[1]", "   ", "[2]", "   ", "[2]", "   ", "[4]", " | "], # # # # # # # # # #
         [" | ", "[5]", "   ", "[6]", "   ", "[7]", "   ", "[8]", "   ", " | "], # Player 2 Pieces
         [" | ", "   ", "[9]", "   ", "[A]", "   ", "[B]", "   ", "[C]", " | "], #
         [" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "]]
boardSize = [10, 10]

# r - row | c - collum
def draw(r = 0, c = 0):
    global board
    global boardSize

    while r < boardSize[0]:
        while c < boardSize[1]:
            print(board[r][c], end="")
            c += 1
        c = 0
        r += 1
        print(end="\n")

# First 12 positions are player 1's pieces and last 12 positions are player 2's pieces
# In sub arrays, positions are stored as [y, x]
piecesPos = [[1, 2], [1, 4], [1, 6], [1, 8], # # # # # # # # # #
             [2, 1], [2, 3], [2, 5], [2, 7], # Player 1 Pieces
             [3, 2], [3, 4], [3, 6], [3, 8], #
             [6, 2], [6, 4], [6, 6], [6, 8], # # # # # # # # # #
             [7, 1], [7, 3], [7, 5], [7, 7], # Player 2 Pieces
             [8, 2], [8, 4], [8, 6], [8, 8],]#


# taking playerInput

def playerInput():
         input = input().split("")
