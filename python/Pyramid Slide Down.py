def longest_slide_down(pyramid):
    copy = [row[:] for row in pyramid]
    for row in range(len(copy) - 2, -1, -1):
        for i in range(len(copy[row])):
            copy[row][i] += max(copy[row + 1][i], copy[row + 1][i + 1])

    return copy[0][0]


if __name__ == '__main__':
    print(longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]))
