base_grid = {
    'A': 'BC/DG/EI/H/F'.split('/'),
    'B': 'EH/A/C/D/F/G/I'.split('/'),
    'C': 'BA/EG/FI/D/H'.split('/'),
    'D': 'EF/A/B/C/G/H/I'.split('/'),
    'E': [*'ABCDFGHI'],
    'F': 'ED/A/B/C/G/H/I'.split('/'),
    'G': 'DA/EC/HI/B/F'.split('/'),
    'H': 'EB/A/C/D/F/G/I'.split('/'),
    'I': 'FC/EA/HG/B/D'.split('/'),
}


def without(point, arr):
    return [p.replace(point, '') for p in arr if p.replace(point, '') != '']


def grid_without_point(grid, point):
    copy = grid.copy()
    del copy[point]
    return dict([(k, without(point, v)) for k, v in copy.items()])


def count_patterns_from(fp, length):
    def _count_patterns_from(p, grid, generation):
        if generation == 1:
            return 1

        return sum([_count_patterns_from(p2[0], grid_without_point(grid, p), generation - 1) for p2 in grid[p]])

    return 0 if length == 0 else _count_patterns_from(fp, base_grid, length)


def test_codewars():
    assert count_patterns_from('A', 0) == 0
    assert count_patterns_from('B', 1) == 1
    assert count_patterns_from('C', 2) == 5
    assert count_patterns_from('E', 2) == 8
    assert count_patterns_from('A', 10) == 0
    assert count_patterns_from('E', 14) == 0
    assert count_patterns_from('E', 4) == 256


def test_remove_point():
    assert grid_without_point(base_grid, 'B') == {}
