theBoard = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' '
}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def checkWinner(board, player):
    wins = [
        ['top-L', 'top-M', 'top-R'],
        ['mid-L', 'mid-M', 'mid-R'],
        ['low-L', 'low-M', 'low-R'],
        ['top-L', 'mid-L', 'low-L'],
        ['top-M', 'mid-M', 'low-M'],
        ['top-R', 'mid-R', 'low-R'],
        ['top-L', 'mid-M', 'low-R'],
        ['top-R', 'mid-M', 'low-L'],
    ]
    for line in wins:
        if all(board[pos] == player for pos in line):
            return True
    return False

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    move = input(f"Turn for {turn}. Move on which space? ")

    while move not in theBoard or theBoard[move] != ' ':
        move = input("Invalid move. Choose another space: ")

    theBoard[move] = turn

    if checkWinner(theBoard, turn):
        printBoard(theBoard)
        print(f"Player {turn} wins!")
        break

    turn = 'O' if turn == 'X' else 'X'
else:
    printBoard(theBoard)
    print("It's a tie!")
