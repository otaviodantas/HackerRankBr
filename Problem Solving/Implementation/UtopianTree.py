"""
HackerRank - Algorithms - Implemation
Utopian Tree
"""

def utopianTree(n):
    if n < 3:
        return(n + 1)
    if n % 2 == 0:
        return(utopianTree(n - 2) * 2) + 1
    else:
        return(utopianTree(n - 2) + 1) * 2
