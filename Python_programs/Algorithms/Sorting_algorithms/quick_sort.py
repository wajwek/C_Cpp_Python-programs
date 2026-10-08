test = [9,2,15,8,34,3, 1, 7]
l = 0
r = len(test) - 1
def quick_sort(arr, left, right):
    if left >= right:
        return arr
    pivot = arr[(right + left) // 2]
    p_left = left
    p_right = right
    while p_left <= p_right:
        while arr[p_left] < pivot:
            p_left += 1
        while arr[p_right] > pivot:
            p_right -= 1
        if p_left <= p_right:
            arr[p_left], arr[p_right] = arr[p_right], arr[p_left]
            p_left += 1
            p_right -= 1
    quick_sort(arr, left, p_left - 1)
    quick_sort(arr, p_left, right)
    return arr
print(quick_sort(test, l, r))
