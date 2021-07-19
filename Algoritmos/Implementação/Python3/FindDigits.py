# hackerrank.com/challenges/find-digits/problem
# score: 25

def findDigits(n):
    return sum((int(i) != 0) and (n % int(i) == 0) for i in str(n))