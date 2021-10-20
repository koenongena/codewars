def dig_pow(n, p):
    digits = map(int, str(n))
    s = sum([digit ** (i + p) for i, digit in enumerate(digits)])
    return s // n if s % n == 0 else -1


if __name__ == '__main__':
    print(dig_pow(89, 1))
    print(dig_pow(46288, 3))
