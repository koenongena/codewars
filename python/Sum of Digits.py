def digits(n):
    return [int(d) for d in str(n)]


def digital_root(n):
    return n if n < 10 else digital_root(sum(digits(n)))


if __name__ == '__main__':
    # print(digits(132189))
    print(digital_root(132189))
