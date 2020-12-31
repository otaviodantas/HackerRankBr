# hackerrank.com/challenges/insertionsort1
# score: 30


def insertionSort1(n, arr):
    for i in range(1, n):
        current_value = arr[i]
        preview_value = i - 1
        while preview_value >= 0 and current_value < arr[preview_value]:
            arr[preview_value + 1] = arr[preview_value]
            preview_value -= 1
            print(*arr)
        arr[preview_value + 1] = current_value

    print(*arr)
