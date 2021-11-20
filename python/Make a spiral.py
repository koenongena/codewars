def flipped(spiral):
    return [list(reversed(row)) for row in reversed(spiral)]


def spiralize(size):
    if size == 3:
        return [[1, 1, 1], [0, 0, 1], [1, 1, 1]]
    elif size == 4:
        return [[1, 1, 1, 1], [0, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]]


    spiral = []
    spiral.append([1] * size) # first row, full of 1s
    spiral.append([0] * (size - 1) + [1]) # second row, full of 0s except the last column
    # From here, we can calculate a spiral of size -2 and flip it over x and y
    # We insert it the "inner spiral" and end the row with 0, 1
    inner_spiral = flipped(spiralize(size - 2))
    for ir in inner_spiral:
        spiral.append(ir + [0, 1])
    # The last row needs a correction: the second last entry shouldn't be a 0, but a one.
    spiral[-1][-2] = 1
    return spiral


def test_spiralize():
    assert spiralize(5) == [[1, 1, 1, 1, 1],
                            [0, 0, 0, 0, 1],
                            [1, 1, 1, 0, 1],
                            [1, 0, 0, 0, 1],
                            [1, 1, 1, 1, 1]]

    assert spiralize(8) == [[1, 1, 1, 1, 1, 1, 1, 1],
                            [0, 0, 0, 0, 0, 0, 0, 1],
                            [1, 1, 1, 1, 1, 1, 0, 1],
                            [1, 0, 0, 0, 0, 1, 0, 1],
                            [1, 0, 1, 0, 0, 1, 0, 1],
                            [1, 0, 1, 1, 1, 1, 0, 1],
                            [1, 0, 0, 0, 0, 0, 0, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1]]
