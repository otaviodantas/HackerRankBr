"""
HackerRank - Algorithms - Implemation
Angry Professor
"""

def angryProfessor(k, a):
    count = 0
    for i in a:
        if i < 1:
            count += 1
    return 'YES' if count < k else 'NO'

    # present = len([x for x in a if x < 1])
    # if present >= k:
    #     return 'NO'
    # else:
    #     return 'YES'
