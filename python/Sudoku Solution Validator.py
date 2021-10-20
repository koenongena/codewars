def valid(arr):
    return sorted(arr) == list(range(1, 10))


def extract_grids(rows):
    return [[rows[row + i][col + j] for i in range(3) for j in range(3)] for row in (0, 3, 6) for col in (0, 3, 6)]


def valid_solution(board):
    rows = [row for row in board]
    columns = [list((row[col] for row in rows)) for col in range(len(board))]
    grids = extract_grids(rows)
    return all(map(valid, rows)) and all(map(valid, columns)) and all(map(valid, grids))


if __name__ == '__main__':
    print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                          [6, 7, 2, 1, 9, 5, 3, 4, 8],
                          [1, 9, 8, 3, 4, 2, 5, 6, 7],
                          [8, 5, 9, 7, 6, 1, 4, 2, 3],
                          [4, 2, 6, 8, 5, 3, 7, 9, 1],
                          [7, 1, 3, 9, 2, 4, 8, 5, 6],
                          [9, 6, 1, 5, 3, 7, 2, 8, 4],
                          [2, 8, 7, 4, 1, 9, 6, 3, 5],
                          [3, 4, 5, 2, 8, 6, 1, 7, 9]]))
