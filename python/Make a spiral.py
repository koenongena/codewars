def flipped(spiral):
    return [list(reversed(row)) for row in reversed(spiral)]  # reversing rows


def spiralize(size):
    if size == 3:
        return [[1, 1, 1], [0, 0, 1], [1, 1, 1]]
    elif size == 4:
        return [[1, 1, 1, 1], [0, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]]

    spiral = init_top_right_and_bottom(size, 1)
    inner_spiral = flipped(spiralize(size - 2))

    for i in range(2, size):
        for j in range(0, size - 2):
            spiral[i][j] = inner_spiral[i - 2][j]

    return spiral


def init_top_right_and_bottom(size, value):
    spiral = [[0 for _ in range(size)] for _ in range(size)]
    spiral[0] = [value for _ in range(size)]
    for row in spiral:
        row[-1] = value
    spiral[-1] = [value for _ in range(size)]
    return spiral


def test_spiralize():
    # assert spiralize(5) == [[1, 1, 1, 1, 1],
    #                         [0, 0, 0, 0, 1],
    #                         [1, 1, 1, 0, 1],
    #                         [1, 0, 0, 0, 1],
    #                         [1, 1, 1, 1, 1]]

    assert spiralize(8) == [[1, 1, 1, 1, 1, 1, 1, 1],
                            [0, 0, 0, 0, 0, 0, 0, 1],
                            [1, 1, 1, 1, 1, 1, 0, 1],
                            [1, 0, 0, 0, 0, 1, 0, 1],
                            [1, 0, 1, 0, 0, 1, 0, 1],
                            [1, 0, 1, 1, 1, 1, 0, 1],
                            [1, 0, 0, 0, 0, 0, 0, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1]]
