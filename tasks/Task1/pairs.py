def filter_pairs(numbers, sum_filter=10):
    numbers_map = list(map(int, numbers))
    n = len(numbers_map)
    pairs = []
    for x in range(0, n):
        for y in range(x + 1, n):
            if numbers_map[x] + numbers_map[y] == sum_filter:
                pairs.append((numbers_map[x], numbers_map[y]))
    if not pairs:
        print("There are no numbers in the list that are equal to %s" % sum_filter)
    return pairs


def print_pairs(pairs):
    for a, b in pairs:
        print(str(a) + " + " + str(b))


if __name__ == '__main__':
    import sys

    print_pairs(filter_pairs(sys.argv[1:]))
