# hackerrank.com/challenges/divisible-sum-pairs
# score: 10


def divisibleSumPairs(n, k, ar):
    count = 0
    for number in range(n - 1):
        next_n = number + 1
        while next_n < n:
            sum = ar[number] + ar[next_n]
            if sum % k == 0:
                count += 1
            next_n += 1
    return count
