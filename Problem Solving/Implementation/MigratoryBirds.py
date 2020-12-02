"""
HackerRank - Algorithms - Implemation
Migratory Birds
"""

def migratoryBirds(arr):
    count = [0]*len(arr)
    for t in arr:
        count[t] += 1
    return(count.index(max(count)))
