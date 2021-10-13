from math import prod


def persistence(n):
    def digits(number):
        return map(int, str(number))

    return 0 if n < 10 else 1 + persistence(prod(digits(n)))


if __name__ == '__main__':
    print(persistence(999))
