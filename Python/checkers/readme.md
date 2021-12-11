# Checkers
## rules
- The arrangement of the game board

![alt text](https://m.media-amazon.com/images/I/71NnA4HYG+L._AC_SX679_.jpg) 

- can only move once per turn 
- each piece can only move _forward_ 1 space diagonally towards an empty space
- once the piece reaches the end of the board they become a "King"
    - King can move 1 space diagonally forwards or backwards
- can jump over one of opponent's piece to capture them
    - once captured, remove from the board
    - must still land in an empty spot
- if all moveable squares are occupied the piece is locked and it cannot be moved
- capture all of the opponent's pieces to win

## sudo code
win = False
while(!win)
- input()
    - take input from player 
        - which piece, left or right

- logic()
    - can the piece move there
        - if not return to input()
    - who win?
        - print name
        - win = True


- draw()
    - the game board
    - the pieces
    - updating the pieces moved by the player


