import pytest


def extract_row(board, r):
    return board[r]


def extract_column(board, col):
    return list((row[col] for row in board))


def extract_block(board, row, col):
    r, c = (row // 3) * 3, (col // 3) * 3

    return [board[r + i][c + j] for i in range(3) for j in range(3)]


def find_possibilities(board, row, col):
    return list(set(range(1, 10))
                - set(extract_row(board, row))
                - set(extract_column(board, col))
                - set(extract_block(board, row, col))
                )


def contains_unknown(rows):
    for row in rows:
        for cell in row:
            if cell == 0:
                return True

    return False


def sudoku(puzzle):
    while contains_unknown(puzzle):
        for r, row in enumerate(puzzle):
            for c, cell in enumerate(row):
                if cell == 0:
                    possibilities = find_possibilities(puzzle, r, c)
                    if len(possibilities) == 1:
                        puzzle[r][c] = possibilities[0]

    return puzzle


@pytest.fixture
def board():
    return [[5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]]


def test_extract_row(board):
    assert extract_row(board, 1) == board[1]


def test_extract_column(board):
    assert extract_column(board, 2) == [4, 2, 8, 9, 6, 3, 1, 7, 5]


def test_extract_block(board):
    assert extract_block(board, 1, 2) == [5, 3, 4, 6, 7, 2, 1, 9, 8]
    assert extract_block(board, 5, 7) == [4, 2, 3, 7, 9, 1, 8, 5, 6]


@pytest.fixture()
def unsolved_board():
    return [[5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def test_find_possibilities(unsolved_board):
    assert find_possibilities(unsolved_board, 0, 2) == [1, 2, 4]


def test_solve_sudoku(unsolved_board):
    solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9]]

    assert sudoku(unsolved_board) == solution

def test_solve_hard_sudoku():
    problem = [[9, 0, 0, 0, 8, 0, 0, 0, 1],
               [0, 0, 0, 4, 0, 6, 0, 0, 0],
               [0, 0, 5, 0, 7, 0, 3, 0, 0],
               [0, 6, 0, 0, 0, 0, 0, 4, 0],
               [4, 0, 1, 0, 6, 0, 5, 0, 8],
               [0, 9, 0, 0, 0, 0, 0, 2, 0],
               [0, 0, 7, 0, 3, 0, 2, 0, 0],
               [0, 0, 0, 7, 0, 5, 0, 0, 0],
               [1, 0, 0, 0, 4, 0, 0, 0, 7]]

    assert sudoku(problem) == None
