N = 4

board = [[0]* N for i in range(N)]


def print_board(board):
    for row in board:
        print(' '.join('Q' if x else '.' for x in row))

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nq_util(board, col):
    if col >= N:
        return True

    for i in range(N):

        if is_safe(board, i, col):
   
            board[i][col] = 1
            
 
            if solve_nq_util(board, col + 1) == True:       
                return True
            
     
            board[i][col] = 0
    
    return False

def solve(board):
    if not solve_nq_util(board, 0):
        print("Solution does not exist")
        return False
    
    print_board(board)
    return True


solve(board)


    


# i = 0           i = 1       i = 2           i = 3
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]