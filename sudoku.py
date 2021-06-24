class sudoku():
    
    def genBoard():
        from random import sample
        tileLength  = 3
        boardLength = 9

        def pattern(r,c):
            return (tileLength*(r%tileLength)+r//tileLength+c)%boardLength

        tile = range(3)

        rows = [i * tileLength + ii for i in sample(tile,3) for ii in sample(tile,3)]
        cols = [i * tileLength + ii for i in sample(tile,3) for ii in sample(tile,3)]

        nums = sample(range(1,10),9)

        board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

        return board

    def redBoard(board):
        from random import sample, randint
        reduced_board = board
        for line in reduced_board:
            for i in sample(range(0,9),randint(5,7)):
                line[i] = ' '
        return reduced_board
        
    def printBoard(board):
        print('_______________________________________________________')
        for idx, line in enumerate(board):
            for i in range(9):
                if i == 0 or i == 3 or i == 6: print('| ', str(line[i]), ' ', end = '')
                else: print('  ', str(line[i]), ' ', end = '')
            print('|')
            if idx == 2 or idx == 5: print('|-----------------------------------------------------|')
            elif idx != 8: print('|                                                     |')
        print('|_____________________________________________________|')

    def solveBoard(board):
        ndx = sudoku.findEmpty(board)
        i,j = ndx
        
        #board[2][2] = 5

        #board[3][2] = 5
        sudoku.violation(board)
        

    def findEmpty(board):
        for i in range(len(board)):
            for ii in range(len(board[0])):
                if board[i][ii] == 0:
                    return(i,ii)
        return None
    
    def violation(board):
        for line in board:
            list = []
            for i in range(len(line)):
                if line[i] == ' ': continue
                if line[i] in list:
                    print('Found a duplicate!')
                    return True
                elif line[i] != ' ': list.append(line[i])

        for i in range(len(board)):
            list = []
            col = board[i]
            for ii in range(len(col)):
                if col[ii] == ' ': continue
                if col[ii] in list:
                    print('Found a duplicate!')
                    return True
                elif col[ii] != ' ': list.append(col[ii])
        return False

#########################################################################################
# Script area #

#board = sudoku.genBoard()
board = [
    [6, 2, 5, 8, 4, 3, 7, 9, 1],
    [7, 9, 1, 2, 6, 5, 4, 8, 3],
    [4, 8, 3, 9, 7, 1, 6, 2, 5],
    [8, 1, 4, 5, 9, 7, 2, 3, 6],
    [2, 3, 6, 1, 8, 4, 9, 5, 7],
    [9, 5, 7, 3, 2, 6, 8, 1, 4],
    [5, 6, 9, 4, 3, 2, 1, 7, 8],
    [3, 4, 2, 7, 1, 8, 5, 6, 9],
    [1, 7, 8, 6, 5, 9, 3, 4, 2]
    ]
sudoku.printBoard(board)
game_board = sudoku.redBoard(board)
sudoku.solveBoard(game_board)
sudoku.printBoard(game_board)
