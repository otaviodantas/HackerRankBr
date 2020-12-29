"""
HackerRank - Algorithms - Implemation
Circular Array Rotation
"""


def circularArrayRotation(a, k, queries):
    n = len(a)
    ans = []
    for q in queries:
        ans.append(a[(n - k + q) % n])
    return ans


if __name__ == '__main__':
    a = [1, 2, 3]
    k = 2
    queries = [0, 1, 2]
    print(circularArrayRotation(a, k, queries))


lista = [1, 2, 3]
print(lista[-1 + 1])
