# Horizontal first 3 tuple - Vertical second 3 tuple - Diagonal third 2 tuple
def find_blocking_spot(position1, position2):
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    marks = ['X', 'O']
    for mark in marks:
        board[position1] = mark
        if is_winner(board):
            return find_blocking_position(board, position1, position2)
        board[position1] = ' '
        board[position2] = mark
        if is_winner(board):
            return find_blocking_position(board, position2, position1)
        board[position2] = ' '
    return None
def is_winner(board):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
]
    for positions in winning_positions:
        if board[positions[0]] == board[positions[1]] == board[positions[2]] != ' ':
            return True
    return False
def find_blocking_position(board, mark_position, other_position):
    blocking_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
]
    for positions in blocking_positions:
        if mark_position in positions and other_position in positions:
            for position in positions:
                if position != mark_position and position != other_position and board[position] == ' ':
                    return position
    return None 
