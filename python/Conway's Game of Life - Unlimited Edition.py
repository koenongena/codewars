from copy import deepcopy
from itertools import product


def surround_with_dead_cells(cells):
    new_cells = cells[:]
    new_cells.insert(0, [0] * len(cells[0]))
    new_cells.append([0] * len(cells[0]))
    return [[0] + row + [0] for row in new_cells]


def neighbours(matrix, row, column):
    neighbours_coords = [(c + column, r + row) for (r, c) in product([-1, 0, 1], [-1, 0, 1]) if (c != 0 or r != 0)]
    return [matrix[r][c] for (c, r) in neighbours_coords if 0 <= r < len(matrix) and 0 <= c < len(matrix[0])]


def count_live_neighbours(cells, row, column):
    return sum(neighbours(cells, row, column))


def crop(matrix):
    if sum(matrix[0]) == 0:
        return crop(matrix[1:])

    if sum(matrix[-1]) == 0:
        return crop(matrix[:-1])

    if sum([row[0] for row in matrix]) == 0:
        return crop([row[1:] for row in matrix])

    if sum([row[-1] for row in matrix]) == 0:
        return crop([row[:-1] for row in matrix])

    return matrix


def get_generation(cells, generations):
    if generations == 0:
        return crop(cells)

    start = surround_with_dead_cells(cells)
    end = deepcopy(start)

    for row_index, row in enumerate(start):
        for col_index, cell in enumerate(row):
            live_neighbours = count_live_neighbours(start, row_index, col_index)
            if cell == 0 and live_neighbours == 3:
                end[row_index][col_index] = 1
            elif cell == 1 and live_neighbours < 2:
                end[row_index][col_index] = 0
            elif cell == 1 and live_neighbours > 3:
                end[row_index][col_index] = 0
            elif cell == 1 and 2 <= live_neighbours <= 3:
                end[row_index][col_index] = 1

    return get_generation(crop(end), generations - 1)


if __name__ == '__main__':
    start = [[1, 0, 0],
             [0, 1, 1],
             [1, 1, 0]]

    print(start)
    print(get_generation(start, 1))

    start = [[1, 1, 1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1, 1, 1]]
    print(get_generation(start, 10))
