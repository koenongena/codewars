def mix(s1, s2):
    result = []
    for letter in set(s1 + s2):
        s1_count = s1.count(letter)
        s2_count = s2.count(letter)

        if not letter.islower() or (max(s1_count, s2_count) < 2):
            continue
        if s1_count > s2_count:
            result.append("1:" + s1_count * letter)
        elif s1_count < s2_count:
            result.append("2:" + s2_count * letter)
        else:
            result.append("=:" + s1_count * letter)

    return '/'.join(sorted(result, key=(lambda x: (-len(x), x))))

if __name__ == '__main__':
    print(mix("Are they here", "yes, they are here"))