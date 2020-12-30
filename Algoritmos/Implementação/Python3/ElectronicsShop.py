# hackerrank.com/challenges/electronics-shop
# score: 10


def getMoneySpent(keyboards, drives, s):
    return max([x + y for x in keyboards for y in drives if x + y <= s]+[-1])
