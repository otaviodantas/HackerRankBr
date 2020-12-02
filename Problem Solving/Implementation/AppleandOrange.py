"""
HackerRank - Algorithms - Implemation
Count Apples and Oranges
"""

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple = [x for x in apples if x+a in range(s,t+1)]
    orange = [x for x in oranges if x+b in range(s,t+1)]
    print(len(apple))
    print(len(orange))
