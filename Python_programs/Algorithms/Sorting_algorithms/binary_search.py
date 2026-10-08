test = [1, 2, 3, 7, 8, 9, 15, 34]
n = len(test)

def binary_search(arr, target, n):
    l = 0
    r = n - 1
    while arr[l] != target:
        middle = (l + r) // 2
        if arr[middle] < target:
            l = middle + 1
        else:
            r = middle - 1
    return arr[l], l
print(binary_search(test, 8, n))
