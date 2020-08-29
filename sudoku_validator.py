"""
Sudoku Solution Validator
Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board,
and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's,
which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.

Examples
validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]); // => true
"""


def valid_solution(board):
    sep = []
    g = []
    b = True
    # Check lines
    for lin in board:
        a = set(lin)
        if 0 in a:
            b = False
        elif len(a) != 9:
            b = False
    # Check columns
    c = zip(*board)
    for ele in c:
        d = set(ele)
        if 0 in d:
            b = False
        elif len(d) != 9:
            b = False
    # Check boxes
    for l in board:
        aux = []
        for x in range(0, len(l), 3):
            chunks = l[x: x + 3]
            aux.append(chunks)
        sep.append(aux)
    k1 = zip(sep[0], sep[1], sep[2])
    k2 = zip(sep[3], sep[4], sep[5])
    k3 = zip(sep[6], sep[7], sep[8])
    m = [k1, k2, k3]
    for k in m:
        for j in k:
            u = set().union(*j)
            g.append(u)
    for o in g:
        if 0 in o:
            b = False
        elif len(o) != 9:
            b = False
    return b


board = [
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]
print(valid_solution(board))

"""
# MY ORIGINAL SOLUTION:

def valid_solution(board):
    sep = []
    g = []
    b = True
    for lin in board:
        a = set(lin)
        if 0 in a:
            b = False
        elif len(a) != 9:
            b = False
    c = zip(board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8])
    for ele in c:
        d = set(ele)
        if 0 in d:
            b = False
        elif len(d) != 9:
            b = False
    for l in board:
        aux = []
        for x in range(0, len(l), 3):
            chunks = l[x: x + 3]
            aux.append(chunks)
        sep.append(aux)
    k1 = zip(sep[0], sep[1], sep[2])
    k2 = zip(sep[3], sep[4], sep[5])
    k3 = zip(sep[6], sep[7], sep[8])
    for j in k1:
        u = set().union(*j)
        g.append(u)
    for j in k2:
        u = set().union(*j)
        g.append(u)
    for j in k3:
        u = set().union(*j)
        g.append(u)
    for o in g:
        if 0 in o:
            b = False
        elif len(o) != 9:
            b = False
    return b

"""

# Simplest codewars solution:
"""
def validSolution(board):
    blocks = [[board[x+a][y+b] for a in (0, 1, 2) for b in (0, 1, 2)] for x in (0, 3, 6) for y in (0, 3, 6)]
    return not filter(lambda x: set(x) != set(range(1, 10)), board + zip(*board) + blocks)
"""