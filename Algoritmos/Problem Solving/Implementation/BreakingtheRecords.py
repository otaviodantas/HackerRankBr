"""
HackerRank - Algorithms - Implemation
Breaking the Records
"""

def breakingRecords(score):
    max_count = min_count = 0
    max = min = score[0]

    for point in score[1:]:
        if point > max:
            max = point
            max_count += 1
        if point < min:
            min = point
            min_count += 1

    return max_count, min_count
