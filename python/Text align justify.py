def justify_line(t, width):
    if ' ' not in t:
        return t

    words = t.split(' ')
    i = 0
    while sum([len(w) for w in words]) < width:
        words[i] = words[i] + ' '
        i = (i + 1) % (len(words) - 1)

    return ''.join(words)


def justify(text, width):
    if len(text) <= width:
        return text
    elif text[width] == ' ':
        return text[0:width] + '\n' + justify(text[width:].strip(), width)

    last_space_index = text.rfind(' ', 0, width)
    return justify_line(text[0: last_space_index].strip(), width) + '\n' + justify(text[last_space_index:].strip(),
                                                                                   width)


def test_codewars():
    assert justify('123 45 6', 7) == '123  45\n6'


def test_simple():
    assert justify('Lorem ipsum dolor', 15) == 'Lorem     ipsum\ndolor'
    assert justify('Lorem ipsum dolor sit amet, consectetur', 15) == 'Lorem     ipsum\ndolor sit amet,\nconsectetur'


def test_single_word_on_line():
    given = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    expected = 'Lorem     ipsum\ndolor sit amet,\nconsectetur\nadipiscing elit'
    assert justify(given, 15) == expected
