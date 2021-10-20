import re


def pig_it(text):
    return re.sub(r'([a-zA-z])([a-zA-z]*)', '\\2\\1ay', text)


if __name__ == '__main__':
    print(pig_it("Pig"))
