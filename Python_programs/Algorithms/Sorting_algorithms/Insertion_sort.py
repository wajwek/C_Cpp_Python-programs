test = [9,2,15,8,34,3, 1, 7]
length = len(test)
def insertionSort2(n, arr):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(*arr)
insertionSort2(length, test)