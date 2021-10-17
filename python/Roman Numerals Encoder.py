def solution(n):
    units = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    return (n // 1000) * 'M' + hundreds[n % 1000 // 100] + tens[n % 100 // 10] + units[n % 10]


if __name__ == '__main__':
    print(solution(1))
    print(solution(1000))
    print(solution(1989))
