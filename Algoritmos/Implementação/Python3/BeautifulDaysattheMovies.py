# hackerrank.com/challenges/beautiful-days-at-the-movies
# score: 15


def beautifulDays(i, j, k):
    c: int = 0
    for n in range(i, j+1):
        to_str = str(n)
        if (n - int(to_str[::-1])) % k == 0:
            c += 1
    return c
