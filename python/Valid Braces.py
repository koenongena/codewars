def validBraces(string):
    opening = '{(['
    closing = '})]'

    history = []
    for b in string:
        if b in closing and (len(history) == 0 or history.pop() != opening[closing.index(b)]):
            return False
        elif b in opening:
            history.append(b)

    return len(history) == 0


if __name__ == '__main__':
    print(validBraces("()"))
    print(validBraces("[(])"))
    print(validBraces("([{}])"))
    print(validBraces("}"))
