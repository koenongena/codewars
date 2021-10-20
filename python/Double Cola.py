import math


def who_is_next(names, r):
    def cycle(t, iteration):
        next_cycle_time = t + iteration * len(names)
        if next_cycle_time > r:
            return t, iteration
        return cycle(next_cycle_time, iteration * 2)

    start, cycle_point = cycle(1, 1)
    return names[(r - start) // cycle_point]




if __name__ == '__main__':
    names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
    # names = ["K", "W"]

    # print(who_is_next(names, 1))
    print(who_is_next(names, 7230702951))
    # print(who_is_next(names, 1))
    # print(who_is_next(names, 52))
    # print(who_is_next(names, 7230702951))

    # assert who_is_next(names, 1) == "Sheldon"
    # assert who_is_next(names, 52) == "Penny"
    # assert who_is_next(names, 7230702951) == "Leonard"
