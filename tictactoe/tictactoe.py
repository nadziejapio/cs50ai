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
    x = 0
    o = 0
    for i in board:
        for j in i:
            if j == X:
                x += 1
            elif j == O:
                o += 1
    return X if x <= o else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    ans = set()
    for i, b in enumerate(board):
        for j, r in enumerate(b):
            if r == EMPTY:
                ans.add((i, j))
    return ans


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError
    new_board = copy.deepcopy(board)
    sign = player(board)
    new_board[action[0]][action[1]] = sign
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] == row[1] == row[2] != None:
            return row[0]
    if board[0][0] == board[1][1] == board[2][2] != None:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != None:
        return board[0][2]
    elif board[0][0] == board[1][0] == board[2][0] != None:
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1] != None:
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2] != None:
        return board[0][2]
    else: 
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    is_Won = winner(board)
    has_actions = actions(board)
    if is_Won != None:
        return True
    elif has_actions != set():
        return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    def maxValue(board):
        if terminal(board):
            return utility(board)
        v = -math.inf
        for action in actions(board):
            v = max(v, minValue(result(board, action)))
            # print(v, minValue(result(board, action)))
            # print(board, action, v)
        return v
    
    def minValue(board):
        if terminal(board):
            return utility(board)
        v = math.inf
        for action in actions(board):
            v = min(v, maxValue(result(board, action)))
            # print(board[0], board[1], board[2], action, v,  sep='\n')
        return v
    
    if player(board) == X:
        act = None
        best_score = -math.inf
        if terminal(board):
            return act
        for action in actions(board):
            score = minValue(result(board, action))
            print(score, action)
            if score > best_score:
                best_score = score
                act = action
        return act
                
    else:
        act = None
        best_score = math.inf
        print('y')
        if terminal(board):
            return act
        for action in actions(board):
            score = maxValue(result(board, action))
            print(score, action)
            if score < best_score:
                best_score = score
                act = action     
        return act