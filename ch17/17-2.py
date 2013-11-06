# X|O|X
# O|X|X
# O|X|O

board = [
    ['X', 'O', 'X'],
    ['O', 'X', 'X'],
    ['O', 'X', 'O'],
]

def someone_won(board):
    """Returns 'X', 'O', or None"""
    # check rows
    for row in board:
        result = all_same(row)
        if result:
            return result
    # check cols
    for i in xrange(len(board)):
        col = []
        for row in board:
            col.append(row[i])
        result = all_same(col)
        if result:
            return result
    # check diagonals
    left_to_right = []
    right_to_left = []
    for i in xrange(len(board)):
        left_to_right.append(board[i][i])
        right_to_left.append(board[i][len(board)-1-i])
    result = all_same(left_to_right)
    if result:
        return result
    result = all_same(right_to_left)
    if result:
        return result
    return None

def all_same(lst):
    if not lst:
        return None
    for i in xrange(len(lst)):
        if lst[i] == '' or (lst[i] != 'X' and lst[i] != 'O'):
            return None
        if lst[i] != lst[0]:
            return None
    return lst[0] # returns 'X' or 'O'
