def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])


if __name__ == '__main__':
    print(sum_two_smallest_numbers([10, 5, 8, 12, 18, 22]))
