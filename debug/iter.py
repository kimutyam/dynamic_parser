from itertools import combinations, permutations, groupby


def debug():
    print(list(combinations([1, 2, 3], 2)))
    c = permutations([1, 2, 3], 3)
    d = groupby([1, 2, 3, 4], lambda x: "gu" if x % 2 == 0 else "ki")
    print(list(c))
    for s, n in d:
        print(s, list(n))