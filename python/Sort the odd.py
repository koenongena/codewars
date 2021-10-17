def sort_array(arr):
    odd = sorted([x for x in arr if x % 2 == 1], reverse=True)
    return [x if x % 2 == 0 else odd.pop() for x in arr]

if __name__ == '__main__':
    print(sort_array([5, 3, 2, 8, 1, 4]))
