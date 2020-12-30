# hackerrank.com/challenges/migratory-birds
# score: 10


def migratoryBirds(arr):
    count = [0]*len(arr)
    for t in arr:
        count[t] += 1
    return(count.index(max(count)))
