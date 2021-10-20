def create_phone_number(n):
    full_digit: str = "".join(map(str, n))
    return '({}) {}-{}'.format(full_digit[:3], full_digit[3:6], full_digit[6:])
    # better alternative: return '({}{}{}) {}{}{}-{}{}{}{}'.format(*n)


if __name__ == '__main__':
    print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
