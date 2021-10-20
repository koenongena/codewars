def unique_in_order(iterable):
    return [x for i, x in enumerate(iterable) if i == 0 or iterable[i - 1] != x]


if __name__ == '__main__':
    print(unique_in_order("AAAABBBCCDAABBBA"))
