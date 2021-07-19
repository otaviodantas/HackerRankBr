# hackerrank.com/challenges/circular-array-rotation
# score: 20


def circularArrayRotation(a, k, queries):
    n = len(a)
    return [a[(n - k + q) % n] for q in queries]
