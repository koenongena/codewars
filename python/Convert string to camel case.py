import re


def to_camel_case(text):
    return re.sub(r'[-_](\w)', lambda g: g.group(1).upper(), text)


if __name__ == '__main__':
    assert to_camel_case('') == ''
    assert to_camel_case("the_stealth_warrior") == "theStealthWarrior"
    assert to_camel_case("The-Stealth-Warrior") == "TheStealthWarrior"
    assert to_camel_case("A-B-C") == "ABC"
