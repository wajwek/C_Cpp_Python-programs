test = [9,2,15,8,34,3, 1, 7]
l = 0
r = len(test) - 1
def merge(arr, left, mid, right):
    p_left = left
    p_mid = mid + 1
    tmp = []
    while p_left <= mid and p_mid <= right:
        if arr[p_left] <= arr[p_mid]:
            tmp.append(arr[p_left])
            p_left += 1
        else:
            tmp.append(arr[p_mid])
            p_mid += 1
    if p_left > mid:
        tmp.extend(arr[p_mid:right + 1])
    else:
        tmp.extend(arr[p_left:mid + 1])

    for i in range(right - left + 1):
        j = i + left
        arr[j] = tmp[i]

def MergeSort(arr, left, right):
    if left == right:
        return None
    middle = (left + right) // 2
    MergeSort(arr, left, middle)
    MergeSort(arr, middle + 1, right)
    merge(arr, left, middle, right)

    return arr

tab_sorted = MergeSort(test, l, r)
print(tab_sorted)

