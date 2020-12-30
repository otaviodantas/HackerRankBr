# hackerrank.com/challenges/angry-professor
# score: 20


def angryProfessor(k, a):
    count = 0
    for i in a:
        if i < 1:
            count = 1
    return 'YES' if count < k else 'NO'
