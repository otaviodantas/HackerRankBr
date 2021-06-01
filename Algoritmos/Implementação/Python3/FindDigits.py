# hackerrank.com/challenges/find-digits/problem
# score: 25

def findDigits(n):
    count_n = 0
     
    for i in str(n):
        if (int(i) != 0) and (n % int(i) == 0):
            count_n += 1
    
    return count_n