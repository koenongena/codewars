def swap(arr):
    return [arr[1], arr[0]]


def next_smaller(n):
    def find_successors_including_zero(digits):
        return sorted([d for d in digits[1:] if d < digits[0]], reverse=True)

    def find_successors_without_zero(digits):
        return sorted([d for d in digits[1:] if d < digits[0] and d != 0], reverse=True)

    def _next_smaller(digits, find_successors=find_successors_without_zero):
        if len(digits) < 2:
            return []
        elif len(digits) == 2:
            return swap(digits) if digits[0] > digits[1] else []

        # Keep the first digit and determine the next smaller number for the rest of the digits
        without_first_digit = _next_smaller(digits[1:], find_successors_including_zero)
        if without_first_digit:
            return [digits[0]] + without_first_digit
        # if there is not next number, try to replace the first digit with a smaller number
        successors = find_successors(digits)
        if successors:
            digits_ = (digits[1:])
            digits_.remove(successors[0])
            digits_.append(digits[0])
            digits_.sort(reverse=True)

            return [successors[0]] + digits_

        return []

    result = _next_smaller(extract_digits(n), find_successors_without_zero)
    return arr_to_number(result) if result else -1


def extract_digits(n):
    return [int(d) for d in str(n)]


def arr_to_number(digits):
    return int(''.join([str(d) for d in digits]))


def test_codewars():
    assert next_smaller(907) == 790
    assert next_smaller(531) == 513
    assert next_smaller(135) == -1
    assert next_smaller(2071) == 2017
    assert next_smaller(414) == 144
    assert next_smaller(123456798) == 123456789
    assert next_smaller(123456789) == -1
    assert next_smaller(1234567908) == 1234567890
    assert next_smaller(219) == 129


def test_codewars_attempt():
    assert next_smaller(1027) == -1
    assert next_smaller(315) == 153
