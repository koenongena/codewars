def swap(arr):
    return [arr[1], arr[0]]


def extract_digits(n):
    return [int(d) for d in str(n)]

def greatest_number_from_digits(digits):
    return arr_to_number(sorted(digits, reverse=True))

def next_smaller(n):
    def next_smaller_in_digits(digits):
        if len(digits) == 1:
            return []
        elif len(digits) == 2:
            return swap(digits) if digits[0] > digits[1] else []

        sub_part = next_smaller_in_digits(digits[1:])
        if sub_part:
            return [digits[0]] + sub_part

        # Maybe the first digits is the one to change?
        # So, find a digits small than the first digit, but not 0
        smaller_than_first_digit = [d for d in digits[1:] if d < digits[0]]
        if smaller_than_first_digit:
            largest_of_the_smaller = sorted(smaller_than_first_digit, reverse=True)[0]
            remaining_digits = digits[:]
            remaining_digits.remove(largest_of_the_smaller)
            return [largest_of_the_smaller] + sorted(remaining_digits, reverse=True)

        return []

    dn = next_smaller_in_digits(extract_digits(n))
    return arr_to_number(dn) if dn and dn[0] != 0 else -1

def arr_to_number(digits):
    return int(''.join([str(d) for d in digits]))


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
