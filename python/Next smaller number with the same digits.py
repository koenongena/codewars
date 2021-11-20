def next_smaller(n):
    digits = list(str(n))

    i = len(digits) - 1
    while i > 0 and digits[i - 1] <= digits[i]: i -= 1
    if i <= 0: return -1

    j = len(digits) - 1
    while digits[j] >= digits[i - 1]: j -= 1
    digits[i - 1], digits[j] = digits[j], digits[i - 1]
    digits[i:] = reversed(digits[i:])
    if digits[0] == '0': return -1
    return int(''.join(digits))

def test_codewars():
    assert next_smaller(9) == -1
    assert next_smaller(10) == -1
    assert next_smaller(12) == -1
    assert next_smaller(21) == 12
    assert next_smaller(907) == 790
    assert next_smaller(531) == 513
    assert next_smaller(135) == -1
    assert next_smaller(2071) == 2017
    assert next_smaller(414) == 144
    assert next_smaller(123456798) == 123456789
    assert next_smaller(123456789) == -1
    assert next_smaller(1234567908) == 1234567890
    assert next_smaller(219) == 192
    assert next_smaller(220) == 202
    assert next_smaller(2013489474370) == 2013489474307


def test_codewars_attempt():
    assert next_smaller(1027) == -1
    assert next_smaller(315) == 153
