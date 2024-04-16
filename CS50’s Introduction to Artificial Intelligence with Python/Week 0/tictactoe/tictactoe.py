"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    cX = sum(row.count('X') for row in board)
    cO = sum(row.count('O') for row in board)
    return X if cX == cO else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    all_possible_actions = set()
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                all_possible_actions.add((row, col))
    return all_possible_actions
    # return {(row, col) for row, row_data in enumerate(board) for col, cell in enumerate(row_data) if cell == EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    valid_actions = actions(board)
    if action not in valid_actions:
        print(action, valid_actions)
        raise Exception("Not valid action")
    
    row, col = action
    board_clone = copy.deepcopy(board)
    board_clone[row][col] = player(board)
    return board_clone
    # row, col = action
    # return [[player(board) if (r, c) == (row, col) else cell for c, cell in enumerate(row_data)] for r, row_data in enumerate(board)]


def checkRow(board, player):
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    return False


def checkCol(board, player):
    for col in range(len(board[0])):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    return False


def checkOneDiagonal(board, player):
    count = 0
    for i in range(len(board)):
        if board[i][i] == player:
            count += 1
    return count == 3


def checkSecondDiagonal(board, player):
    count = 0
    for i in range(len(board)):
        if board[i][len(board) - i - 1] == player:
            count += 1
    return count == 3


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkRow(board, X) or checkCol(board, X) or checkOneDiagonal(board, X) or checkSecondDiagonal(board, X):
        return X
    elif checkRow(board, O) or checkCol(board, O) or checkOneDiagonal(board, O) or checkSecondDiagonal(board, O):
        return O
    else:
        return None
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    moves_left = sum(row.count(EMPTY) for row in board)
    return True if winner(board) or moves_left == 0 else False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    elif player(board) == X:
        plays = []
        for action in actions(board):
            plays.append([min_value(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1]
    
    elif player(board) == O:
        plays = []
        for action in actions(board):
            plays.append([max_value(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0])[0][1]