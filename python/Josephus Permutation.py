def josephus(items, k):
    c = items[::]

    result = []
    index = 0

    while len(c) > 0:
        index = (index + k - 1) % len(c)
        result.append(c.pop(index))

    return result


def test_josephus_simple():
    assert josephus([1, 2, 3, 4, 5, 6, 7], 3) == [3, 6, 2, 7, 5, 1, 4]


def test_josephus_chars():
    assert josephus(["C", "o", "d", "e", "W", "a", "r", "s"], 4) == ['e', 's', 'W', 'o', 'C', 'd', 'r', 'a']
