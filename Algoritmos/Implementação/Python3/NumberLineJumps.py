# hackerrank.com/challenges/kangaroo
# score: 10


def kangaroo(x1, v1, x2, v2):
    return 'YES' if (v1 > v2) and (x1 - x2) % (v1 - v2) == 0 else 'NO'
