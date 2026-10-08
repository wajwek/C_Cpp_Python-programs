def quick_sort_lomuto(arr, left, right, k):

    if left >= right:
        return arr

    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    if i == k:
        return arr[i]
    if i > k:
        quick_sort_lomuto(arr, left, i - 1, k)
    else:
        quick_sort_lomuto(arr, i + 1, right, k)

    return arr

large_matrix = [
    [20, 15, 12,  8],
    [18, 14, 11,  7],
    [15, 10,  9,  5],
    [13,  9,  6,  2]
]
n = 4
