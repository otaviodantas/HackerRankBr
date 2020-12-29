"""
HackerRank - Algorithms - Implemation
Counting Valleys
"""


def countingValleys(steps, path):
    sea = count_valley = 0
    for step in path:
        if step == 'U':
            sea += 1
        else:
            sea -= 1
        if step == 'U' and sea == 0:
            count_valley += 1

    return count_valley
